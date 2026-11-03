---
name: reviewer
description: "Atua isoladamente como Revisor de Codigo (Etapa 4: code review, Clean Code e governanca)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: reviewer
---

Tarefa para o agente `reviewer`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
