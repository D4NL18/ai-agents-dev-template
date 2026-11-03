#!/usr/bin/env python3
"""Converte o template `.agents/` (formato Antigravity/Gemini) para o formato do Claude Code.

Fonte da verdade: .agents/   ->   Saida: .claude/, CLAUDE.md, .mcp.json
Nao altera nem apaga nada em .agents/. Pode ser reexecutado (regenera .claude/ gerado).

Uso:  python3 scripts/sync-claude.py [raiz-do-repo]
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SRC = ROOT / ".agents"
OUT = ROOT / ".claude"

# --- Subagentes: nome original -> (nome claude, tools) ------------------------------------------
RW = ["Read", "Write", "Edit", "Glob", "Grep"]
WEB = ["WebSearch", "WebFetch"]
ASK = ["AskUserQuestion"]
REVIEW = ["Read", "Write", "Glob", "Grep", "Bash"]  # revisores nao editam codigo (sem Edit)

SUBAGENTS = [
    "product_owner", "analyst", "architect", "designer", "dba", "ai_specialist",
    "privacy_officer", "tester", "developer", "reviewer", "ux_reviewer", "security",
    "devops", "finance_advisor", "negotiator", "strategic_leader",
    "ai_governance_auditor", "innovation_consultant", "n8n_specialist",
]


def kebab(name: str) -> str:
    return name.replace("_", "-")


TOOLS = {
    "orchestrator": RW + ["Bash", "TodoWrite"] + ASK,  # + Agent(...) montado abaixo
    "product_owner": RW + ASK,
    "analyst": RW + WEB + ASK,
    "architect": RW + ["Bash"] + WEB + ASK,
    "designer": RW + ["Bash", "WebFetch"] + ASK,
    "dba": RW + ["Bash"],
    "ai_specialist": RW + ["Bash"] + WEB,
    "privacy_officer": RW,
    "tester": RW + ["Bash"],
    "developer": RW + ["Bash", "WebFetch"],
    "reviewer": REVIEW,
    "ux_reviewer": REVIEW,
    "security": REVIEW + ["WebFetch"],
    "devops": RW + ["Bash"],
    "finance_advisor": RW + WEB,
    "negotiator": RW,
    "strategic_leader": RW + WEB,
    "ai_governance_auditor": RW + WEB,
    "innovation_consultant": RW + WEB,
    "n8n_specialist": RW + ["Bash"] + WEB,
}

# Skills "persona" (/po, /developer...): slash command -> subagente correspondente
PERSONA_SKILLS = {
    "po": "product_owner", "analyst": "analyst", "architect": "architect", "designer": "designer",
    "dba": "dba", "developer": "developer", "reviewer": "reviewer", "tester": "tester",
    "security": "security", "devops": "devops", "ai_specialist": "ai_specialist",
    "privacy": "privacy_officer", "finance": "finance_advisor", "negotiator": "negotiator",
    "leader": "strategic_leader", "responsible_ai": "ai_governance_auditor",
    "innovation": "innovation_consultant", "n8n": "n8n_specialist",
}
# Skills que precisam rodar na thread principal (despacham outros subagentes)
MAIN_THREAD_SKILLS = {"o", "orquestrador", "orquestrar", "init"}

SKILL_RENAMES = {"ai_specialist": "ai-specialist", "responsible_ai": "responsible-ai"}


# --- Utilitarios ---------------------------------------------------------------------------------
def read(p: Path) -> str:
    return p.read_text(encoding="utf-8").replace("\r\n", "\n")


def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and p.read_bytes() == text.encode("utf-8"):
        return  # incremental: nao toca o que nao mudou
    p.write_text(text, encoding="utf-8", newline="\n")


def split_fm(text: str):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return "", text
    return m.group(1), m.group(2)


def fm_get(fm: str, key: str):
    m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def fm_list(fm: str, key: str):
    m = re.search(rf"^{key}:\s*\n((?:[ \t]+-.*\n?)+)", fm + "\n", re.M)
    if not m:
        return []
    return [re.sub(r"^[ \t]+-\s*", "", ln).strip().strip('"').strip("'")
            for ln in m.group(1).splitlines() if ln.strip()]


def q(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def rewrite(text: str) -> str:
    """Reescreve referencias do dialeto .agents/ para o dialeto Claude Code."""
    # @imports viram caminhos explicitos para leitura com Read (subagentes nao expandem @)
    text = re.sub(r"@((?:\.agents|\.claude)/[^\s)`,;]*[^\s)`,;.:])", r"`\1`", text)
    text = text.replace("@AGENTS.md", "`AGENTS.md`")
    text = text.replace("`invoke_subagent`", "ferramenta `Agent`")
    text = text.replace("invoke_subagent", "ferramenta `Agent`")
    text = text.replace(".agents/skills/", ".claude/skills/")
    text = text.replace(".agents/agents/", ".claude/agents/")
    # nomes de agentes/skills com underscore -> kebab (Claude exige letras minusculas e hifens)
    for old in sorted(set(SUBAGENTS) | set(SKILL_RENAMES), key=len, reverse=True):
        text = re.sub(rf"(?<![A-Za-z0-9_-]){old}(?![A-Za-z0-9_])", kebab(old), text)
    text = text.replace("`ferramenta `Agent``", "ferramenta `Agent`")
    # rules: model_decision viram skills (rule-*), as demais permanecem em .claude/rules/
    for stem in MODEL_DECISION:
        text = text.replace(f".agents/rules/{stem}.md", f".claude/skills/rule-{stem}/SKILL.md")
    text = text.replace(".agents/rules/", ".claude/rules/")
    text = text.replace(".agents/rules", ".claude/rules")
    return text


# --- 1. Rules ------------------------------------------------------------------------------------
MODEL_DECISION: list[str] = []
report = {"rules": 0, "rule_skills": 0, "agents": 0, "skills": 0, "persona": 0}


def classify_rules():
    for f in sorted((SRC / "rules").glob("*.md")):
        fm, _ = split_fm(read(f))
        if fm_get(fm, "trigger") == "model_decision":
            MODEL_DECISION.append(f.stem)


def convert_rules():
    for f in sorted((SRC / "rules").glob("*.md")):
        fm, body = split_fm(read(f))
        trigger, desc, globs = fm_get(fm, "trigger"), fm_get(fm, "description"), fm_list(fm, "globs")
        body = rewrite(body).lstrip("\n")
        if trigger == "model_decision":
            # Claude Code rules nao tem gatilho semantico; skill com description faz esse papel.
            name = f"rule-{f.stem}"
            header = f"---\nname: {name}\ndescription: {q(desc)}\n---\n\n"
            write(OUT / "skills" / name / "SKILL.md", header + body)
            report["rule_skills"] += 1
        else:
            header = ""
            if trigger == "glob" and globs:
                header = "---\npaths:\n" + "".join(f"  - {q(g)}\n" for g in globs) + "---\n\n"
            # always_on -> sem `paths` => carrega em toda sessao
            write(OUT / "rules" / f.name, header + body)
            report["rules"] += 1


# --- 2. Subagentes -------------------------------------------------------------------------------
ORCH_NOTE = """
## Execução no Claude Code

> [!IMPORTANT]
> Subagentes **não** criam outros subagentes. Por isso o Orquestrador deve rodar como **thread principal**
> (`claude --agent orchestrator`, ou `"agent": "orchestrator"` em `.claude/settings.json`, já configurado).
> - Despache especialistas com a ferramenta `Agent` (`subagent_type` = nome do agente, em kebab-case).
> - Tarefas `[PARALLEL]`: emita várias chamadas `Agent` na **mesma mensagem**, cada uma com seu `STATE_<Frente>.md`.
> - Cada subagente começa com contexto limpo: no prompt do despacho, inclua feature, caminhos dos artefatos
>   de entrada em `.agents/docs/` e o resultado esperado. Peça retorno enxuto (resumo + caminhos dos arquivos gerados).
> - Etapa 2 termina em checkpoint: pare e apresente o resumo ao usuário antes da Etapa 3.
"""


def convert_agents():
    (OUT / "agents").mkdir(parents=True, exist_ok=True)
    for f in sorted((SRC / "agents").glob("*.md")):
        orig = f.stem
        fm, body = split_fm(read(f))
        name = kebab(orig)
        desc = rewrite(fm_get(fm, "description") or "")
        tools = list(TOOLS.get(orig, RW + ["Bash"]))
        if orig == "orchestrator":
            team = ", ".join(kebab(a) for a in SUBAGENTS)
            tools = [f"Agent({team})"] + tools
        body = rewrite(body).lstrip("\n")
        if orig == "orchestrator":
            body = body.rstrip() + "\n" + ORCH_NOTE
        header = (f"---\nname: {name}\ndescription: {q(desc)}\n"
                  f"tools: {', '.join(tools)}\n---\n\n")
        write(OUT / "agents" / f"{name}.md", header + body)
        report["agents"] += 1


# --- 3. Skills -----------------------------------------------------------------------------------
def convert_skills():
    skills_src = SRC / "skills"
    for d in sorted(p for p in skills_src.iterdir() if p.is_dir()):
        name = SKILL_RENAMES.get(d.name, d.name)
        dest = OUT / "skills" / name
        if d.name in PERSONA_SKILLS or d.name in MAIN_THREAD_SKILLS:
            convert_command_skill(d, dest, name)
            continue
        for f in sorted(x for x in d.rglob("*") if x.is_file()):
            target = dest / f.relative_to(d)
            if f.suffix == ".md":
                write(target, rewrite(read(f)))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                if not (target.exists() and target.stat().st_size == f.stat().st_size
                        and target.read_bytes() == f.read_bytes()):
                    shutil.copyfile(f, target)
        report["skills"] += 1


def convert_command_skill(d: Path, dest: Path, name: str):
    fm, body = split_fm(read(d / "SKILL.md"))
    desc = rewrite(fm_get(fm, "description") or "")
    if d.name in PERSONA_SKILLS:
        agent = kebab(PERSONA_SKILLS[d.name])
        text = (
            f"---\nname: {name}\ndescription: {q(desc)}\n"
            f"argument-hint: \"[tarefa]\"\n"
            f"disable-model-invocation: true\ncontext: fork\nagent: {agent}\n---\n\n"
            f"Tarefa para o agente `{agent}`:\n\n$ARGUMENTS\n\n"
            "Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. "
            "Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. "
            "Se a demanda exigir outra especialidade, recomende `/orquestrador`.\n"
        )
        report["persona"] += 1
    else:
        text = (
            f"---\nname: {name}\ndescription: {q(desc)}\n"
            f"argument-hint: \"[demanda]\"\ndisable-model-invocation: true\n---\n\n"
            + rewrite(body).lstrip("\n").rstrip()
            + "\n\n> Execute na thread principal (ela precisa despachar subagentes). Recomendado: `claude --agent orchestrator`.\n"
            "\nDemanda do usuário: $ARGUMENTS\n"
        )
        report["persona"] += 1
    write(dest / "SKILL.md", text)


# --- 4. CLAUDE.md, settings, hooks, MCP ------------------------------------------------------------
CLAUDE_HEADER = """# CLAUDE.md — Fluxo de Desenvolvimento com IA

> Gerado por `scripts/sync-claude.py` a partir de `AGENTS.md` + `.agents/config.md`. Fonte da verdade: `.agents/`.
> Estrutura Claude Code: `.claude/agents/` (subagentes) · `.claude/skills/` (skills + slash commands) · `.claude/rules/` (regras) · `.claude/settings.json` (hooks/permissões).

## Como o Claude Code executa este fluxo
- A sessão roda como o **Orquestrador** (`"agent": "orchestrator"` em `.claude/settings.json`); ele despacha subagentes com a ferramenta `Agent`.
- **Rules:** `.claude/rules/` — as `always_on` carregam em toda sessão; as de glob carregam ao ler arquivos correspondentes. As regras por contexto (`model_decision`) viraram skills `rule-*` com gatilho semântico.
- **Skills:** `.claude/skills/<nome>/SKILL.md`. Cada subagente só deve ler (com `Read`) as skills do seu repertório (tabela abaixo) — anti context bloat.
- **Slash commands:** `/po`, `/developer`, `/security`… rodam o subagente isolado (`context: fork`). `/orquestrador`, `/o`, `/orquestrar`, `/init` rodam na thread principal.
- Para desligar o modo orquestrador padrão, remova a chave `agent` de `.claude/settings.json`.

"""


def build_claude_md():
    agents_md = rewrite(read(ROOT / "AGENTS.md"))
    # remove o titulo original (ja ha H1 no cabecalho)
    agents_md = re.sub(r"^# .*\n", "", agents_md, count=1)
    agents_md = re.sub(r"^Fluxo obrigat[^\n]*\n", "Fluxo obrigatório para qualquer tarefa assistida por IA neste projeto. `.agents/docs/` guarda documentação e estado; o comportamento dos agentes vive em `.claude/`.\n", agents_md, count=1, flags=re.M)
    agents_md = agents_md.replace(" (`subagent: true`)", "")
    # secao 1 do config.md (anti-sobrecarga cognitiva)
    cfg = read(SRC / "config.md")
    m = re.search(r"(## 1\. Regras Anti-Sobrecarga.*?)(?=\n## 2\.)", cfg, re.S)
    extra = "\n---\n\n" + rewrite(m.group(1)).replace("(`config.md`)", "(`CLAUDE.md`)").replace("Etapa 12", "Etapa 5").strip() + "\n" if m else ""
    write(ROOT / "CLAUDE.md", CLAUDE_HEADER + agents_md.strip() + "\n" + extra)


SYNC_HOOK = r"""#!/usr/bin/env node
// PostToolUse (Write|Edit): ao alterar .agents/ (exceto docs/), regenera .claude/ via scripts/sync-claude.py.
// So age em repositorios que possuem scripts/sync-claude.py (os demais repos nao sao afetados).
const { spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");
let raw = "";
process.stdin.on("data", (c) => (raw += c));
process.stdin.on("end", () => {
  try {
    const input = JSON.parse(raw);
    const root = (input.cwd || process.cwd());
    const script = path.join(root, "scripts", "sync-claude.py");
    if (!fs.existsSync(script)) process.exit(0);
    const file = ((input.tool_input && input.tool_input.file_path) || "").replace(/\\/g, "/");
    const r = root.replace(/\\/g, "/").replace(/\/$/, "");
    if (!file.toLowerCase().startsWith(r.toLowerCase() + "/")) process.exit(0);
    const rel = file.slice(r.length + 1);
    const watched = /^(AGENTS\.md|\.agents\/(agents|skills|rules)\/|\.agents\/(config\.md|hooks\.json|mcp_config\.json))/;
    if (!watched.test(rel)) process.exit(0);
    for (const py of ["python3", "python", "py"]) {
      const res = spawnSync(py, [script, root], { encoding: "utf8" });
      if (!res.error) {
        if (res.status !== 0) console.error("sync-claude falhou:\n" + (res.stderr || res.stdout));
        process.exit(0);
      }
    }
    console.error("sync-claude: python nao encontrado");
  } catch (e) {}
  process.exit(0);
});
"""

BLOCK_HOOK = r"""#!/usr/bin/env node
// PreToolUse (Write|Edit): aplica a Regra de Ouro — veto a documentacao na raiz do repositorio.
// Bloqueia (exit 2) criar/editar *.md na raiz, exceto README/CLAUDE/AGENTS/CHANGELOG/CONTRIBUTING/LICENSE.
let raw = "";
process.stdin.on("data", (c) => (raw += c));
process.stdin.on("end", () => {
  try {
    const input = JSON.parse(raw);
    const file = (input.tool_input && input.tool_input.file_path) || "";
    const root = (input.cwd || process.cwd()).replace(/\\/g, "/").replace(/\/$/, "");
    const p = file.replace(/\\/g, "/");
    if (!p.toLowerCase().startsWith(root.toLowerCase() + "/")) process.exit(0);
    const rel = p.slice(root.length + 1);
    if (rel.includes("/") || !/\.(md|mdx|txt)$/i.test(rel)) process.exit(0);
    if (/^(README|CLAUDE|AGENTS|CHANGELOG|CONTRIBUTING|LICENSE|SECURITY|CODE_OF_CONDUCT)(\.[a-z]+)?$/i.test(rel)) process.exit(0);
    console.error(
      `BLOQUEADO: documentação na raiz é proibida (${rel}). Salve em .agents/docs/ ` +
      `(business_rules/, api_contracts/, db/, design/, tasks/, adr/, privacy/ ...). Ver .claude/rules/workflow-documentation-governance-rules.md`
    );
    process.exit(2);
  } catch (e) {
    process.exit(0); // nunca quebrar a sessao por falha do hook
  }
});
"""


def build_settings():
    orig = {}
    hp = SRC / "hooks.json"
    if hp.exists():
        orig = json.loads(read(hp))
    stop_hooks = []
    for _group, events in orig.items():
        for cmd in events.get("Stop", []):
            c = cmd.get("command", "")
            # guarda: so roda se o projeto tiver package.json (template e agnostico de stack)
            guarded = f"[ -f package.json ] && {{ {c}; }} || true"
            stop_hooks.append({"type": "command", "command": guarded, "timeout": cmd.get("timeout", 60)})
    settings = {
        "$schema": "https://json.schemastore.org/claude-code-settings.json",
        "agent": "orchestrator",
        "permissions": {"deny": ["Read(./.env)", "Read(./.env.*)", "Read(./secrets/**)"]},
        "hooks": {
            "PostToolUse": [{
                "matcher": "Write|Edit",
                "hooks": [{"type": "command", "command": "node .claude/hooks/sync-on-agents-edit.cjs", "timeout": 180}],
            }],
            "PreToolUse": [{
                "matcher": "Write|Edit",
                "hooks": [{"type": "command", "command": "node .claude/hooks/block-root-docs.mjs", "timeout": 10}],
            }],
            "Stop": [{"hooks": stop_hooks}] if stop_hooks else [],
        },
    }
    if not settings["hooks"]["Stop"]:
        del settings["hooks"]["Stop"]
    write(OUT / "settings.json", json.dumps(settings, indent=2, ensure_ascii=False) + "\n")
    write(OUT / "hooks" / "block-root-docs.mjs", BLOCK_HOOK)
    write(OUT / "hooks" / "sync-on-agents-edit.cjs", SYNC_HOOK)


def build_mcp():
    mp = SRC / "mcp_config.json"
    example = json.loads(read(mp)) if mp.exists() else {"mcpServers": {}}
    # exemplo (com credenciais de mentira) fica fora de .mcp.json para nao ser carregado como servidor real
    write(OUT / "mcp.example.json", json.dumps(example, indent=2, ensure_ascii=False) + "\n")
    target = ROOT / ".mcp.json"
    if not target.exists():
        write(target, json.dumps({"mcpServers": {}}, indent=2) + "\n")


def main():
    if not SRC.is_dir():
        sys.exit(f"{SRC} nao encontrado")
    classify_rules()
    convert_rules()
    convert_agents()
    convert_skills()
    build_claude_md()
    build_settings()
    build_mcp()
    print(json.dumps(report, indent=2))


main()
