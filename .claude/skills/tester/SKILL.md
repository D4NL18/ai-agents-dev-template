---
name: tester
description: "Atua isoladamente como Tester (QA/TDD) (Etapas 3 e 4: TDD, validacao e Auto-Healer)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: tester
---

Tarefa para o agente `tester`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
