---
name: analyst
description: "Atua isoladamente como Analista (Etapa 1: discovery, regras P-XXX e escopo da tarefa)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: analyst
---

Tarefa para o agente `analyst`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
