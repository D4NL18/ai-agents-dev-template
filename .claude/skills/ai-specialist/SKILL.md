---
name: ai-specialist
description: "Atua isoladamente como Especialista em IA (Etapas 2 e 3: ML, RAG, LLMs, CV e tokenomics)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: ai-specialist
---

Tarefa para o agente `ai-specialist`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
