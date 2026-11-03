#!/usr/bin/env node
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
