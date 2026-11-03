---
name: privacy
description: "Atua isoladamente como Encarregado de Dados (DPO/LGPD) (Etapas 2 e 4 ou consultoria LGPD sob demanda)."
argument-hint: "[tarefa]"
disable-model-invocation: true
context: fork
agent: privacy-officer
---

Tarefa para o agente `privacy-officer`:

$ARGUMENTS

Se nenhuma tarefa foi informada, leia `.agents/docs/STATE.md` e siga a etapa em andamento. Salve todo artefato exclusivamente em `.agents/docs/` (veto à raiz) e registre o progresso no `STATE.md`. Se a demanda exigir outra especialidade, recomende `/orquestrador`.
