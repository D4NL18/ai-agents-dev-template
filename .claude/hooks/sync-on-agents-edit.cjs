#!/usr/bin/env node
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
