---
name: po
description: "Atua isoladamente como Product Owner (Etapa 1: fatiamento INVEST e backlog no ROADMAP.md)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: product-owner
---

Tarefa para o agente `product-owner`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
