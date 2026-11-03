---
name: n8n
description: "Atua isoladamente como Especialista N8N (Auxiliar: workflows, bots, integracoes, RAG, MultiAgentes e MCP no N8N)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: n8n-specialist
---

Tarefa para o agente `n8n-specialist`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
