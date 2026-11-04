#!/usr/bin/env python3
"""Instala agents, skills e rules do template no Claude Code do USUARIO (~/.claude), valendo em todos os projetos.

Uso (na raiz do repo ai-agents-dev-template):
    python scripts/install-claude-global.py              # instala/atualiza
    python scripts/install-claude-global.py --dry-run    # mostra o que faria, sem gravar
    python scripts/install-claude-global.py --uninstall  # remove somente o que este script instalou
Opcoes: --no-sync (nao regenera .claude/ antes), --force (sobrescreve arquivos seus de mesmo nome)

- Origem: .claude/{agents,skills,rules} deste repo (gerado por sync-claude.py a partir de .agents/).
- Destino: ~/.claude (ou $CLAUDE_CONFIG_DIR). Um manifesto (.agents-template-manifest.json) registra o que foi instalado,
  entao reinstalar atualiza/remove obsoletos e --uninstall nao toca em nada seu.
- Caminhos `.claude/skills|rules|agents/...` dentro dos textos viram caminhos absolutos do destino,
  pois em outros projetos nao existe .claude/ local.
- NAO instala: settings.json, hooks, .mcp.json, CLAUDE.md (sao por projeto).
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ARGS = set(sys.argv[1:])
DRY, UNINSTALL, FORCE, NO_SYNC = "--dry-run" in ARGS, "--uninstall" in ARGS, "--force" in ARGS, "--no-sync" in ARGS

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / ".claude"
DEST = Path(os.environ.get("CLAUDE_CONFIG_DIR") or (Path.home() / ".claude")).expanduser().resolve()
MANIFEST = DEST / ".agents-template-manifest.json"
KINDS = ("agents", "skills", "rules")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {}


def prune_empty_dirs(start: Path):
    p = start
    while p != DEST and p.exists() and not any(p.iterdir()):
        p.rmdir()
        p = p.parent


def uninstall():
    man = load_manifest()
    if not man:
        print("Nada a remover (manifesto nao encontrado).")
        return
    removed = changed = 0
    for rel, digest in man.items():
        f = DEST / rel
        if not f.exists():
            continue
        if sha(f.read_bytes()) != digest and not FORCE:
            print(f"  mantido (editado por voce): {rel}")
            changed += 1
            continue
        print(f"  remove: {rel}")
        if not DRY:
            f.unlink()
            prune_empty_dirs(f.parent)
        removed += 1
    if not DRY and not changed:
        MANIFEST.unlink(missing_ok=True)
    print(f"\n{'[dry-run] ' if DRY else ''}removidos: {removed} | mantidos por edicao local: {changed}")


def transform(rel: str, data: bytes) -> bytes:
    if not rel.endswith(".md"):
        return data
    base = DEST.as_posix()
    text = data.decode("utf-8")
    text = re.sub(r"(?<![\w/])\.claude/(skills|rules|agents)/", lambda m: f"{base}/{m.group(1)}/", text)
    return text.encode("utf-8")


def install():
    if not SRC.is_dir():
        sys.exit(f"{SRC} nao existe. Rode: python scripts/sync-claude.py .")
    sync = REPO / "scripts" / "sync-claude.py"
    if not NO_SYNC and sync.exists() and not DRY:
        print("Sincronizando .claude/ a partir de .agents/ ...")
        subprocess.run([sys.executable, str(sync), str(REPO)], check=True, stdout=subprocess.DEVNULL)

    old = load_manifest()
    new: dict[str, str] = {}
    stats = {"novo": 0, "atualizado": 0, "igual": 0, "conflito": 0, "obsoleto": 0}

    for kind in KINDS:
        base = SRC / kind
        if not base.is_dir():
            continue
        for f in sorted(p for p in base.rglob("*") if p.is_file()):
            rel = f"{kind}/{f.relative_to(base).as_posix()}"
            data = transform(rel, f.read_bytes())
            digest = sha(data)
            target = DEST / rel
            if target.exists():
                cur = sha(target.read_bytes())
                if cur == digest:
                    stats["igual"] += 1
                    new[rel] = digest
                    continue
                if rel not in old and not FORCE:
                    print(f"  CONFLITO (arquivo seu, mantido): {rel}  [use --force para sobrescrever]")
                    stats["conflito"] += 1
                    continue
                stats["atualizado"] += 1
            else:
                stats["novo"] += 1
            if not DRY:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            new[rel] = digest

    # remove o que foi instalado antes e nao existe mais na origem
    for rel, digest in old.items():
        if rel in new:
            continue
        f = DEST / rel
        if f.exists() and sha(f.read_bytes()) == digest:
            if not DRY:
                f.unlink()
                prune_empty_dirs(f.parent)
            stats["obsoleto"] += 1

    if not DRY:
        DEST.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps(new, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\n{'[dry-run] ' if DRY else ''}destino: {DEST}")
    print(", ".join(f"{k}: {v}" for k, v in stats.items()))
    if not DRY:
        print("\nPronto. Abra um projeto qualquer no Claude Code: /orquestrador, /po, /developer ... ja estarao disponiveis.")
        print("Para o modo orquestrador no projeto: claude --agent orchestrator")


if UNINSTALL:
    uninstall()
else:
    install()
