---
name: finance
description: "Atua isoladamente como Conselheiro Financeiro (Auxiliar: DRE, VPL, TIR, Capex/Opex e Unit Economics)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: finance-advisor
---

Tarefa para o agente `finance-advisor`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
