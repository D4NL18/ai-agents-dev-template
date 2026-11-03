---
name: dba
description: "Atua isoladamente como DBA (Etapa 2: migrations seguras, schema e seeds)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: dba
---

Tarefa para o agente `dba`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
