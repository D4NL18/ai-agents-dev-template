---
name: init
description: "Kickoff de novo projeto - Brainstorming Global com Arquiteto, DBA, Designer, PO e DevOps para gerar DESIGN_SYSTEM.md, GLOSSARY.md, ARCHITECTURE.md e ROADMAP.md em .agents/docs/."
argument-hint: "[demanda]"
disable-model-invocation: true
---

# Execucao do Workflow /init (Fundacao do Projeto)

1. Leia imediatamente `.claude/agents/orchestrator.md`, `AGENTS.md` e `.agents/docs/STATE.md`. Assuma o papel de Orquestrador.
2. **Brainstorming Global com o usuario** (perguntas objetivas sobre produto, publico, stack, dados, IA e restricoes de custo/LGPD). Invoque via ferramenta `Agent`:
   - `architect` -> consolida `.agents/docs/architecture/ARCHITECTURE.md` e ADRs iniciais em `.agents/docs/adr/`.
   - `dba` -> define a estrategia de dados (SGBD, padroes de migration, LGPD) e documenta em `.agents/docs/db/`.
   - `designer` (se houver Frontend) -> gera `.agents/docs/design/DESIGN_SYSTEM.md` a partir de `.agents/docs/design/TEMPLATE_DESIGN_SYSTEM.md`, com filtro Anti-IA.
   - `analyst` (skill `domain-expert`) -> inicia `.agents/docs/GLOSSARY.md` com a linguagem ubiqua.
3. Invoque `product-owner` para fatiar o backlog inicial em User Stories INVEST em `.agents/docs/ROADMAP.md`, marcando `[PARALLEL]`.
4. Invoque `devops` para a fundacao do repositorio (estrutura, CI/CD base, Docker multi-stage, FinOps) e sincronize `.agents/hooks.json` e `.agents/mcp_config.json` com a stack escolhida.
5. Atualize `.agents/docs/STATE.md` com o resumo do kickoff e apresente ao usuario os artefatos gerados. Nenhum arquivo de documentacao pode ser salvo na raiz do repositorio.

> Execute na thread principal (ela precisa despachar subagentes). Recomendado: `claude --agent orchestrator`.

Demanda do usuário: $ARGUMENTS
