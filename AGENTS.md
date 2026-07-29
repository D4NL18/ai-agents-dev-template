# Fluxo de Desenvolvimento com IA (AI Agents Workflow)

Este documento define o fluxo obrigatório para qualquer tarefa de desenvolvimento assistida por Inteligência Artificial neste projeto. O diretório `.agents/` contém o detalhamento individual de cada papel.

## Fluxo de Trabalho (Workflow - 10 Passos)

Todo prompt ou nova requisição deve obrigatoriamente seguir as seguintes etapas na ordem estabelecida.

1. **Especificar (Specification)**
   - O **Analista** amarra regras de negócio (P-XXX) e define o escopo.

2. **Projetar (Design & Architecture)**
   - O **Arquiteto** define a arquitetura técnica, banco de dados, APIs (`api-contracts`).
   - O **Designer** (se envolver Frontend) projeta as diretrizes visuais (UI/UX).

3. **Modelagem de Dados Segura (DBA)**
   - O **DBA** traduz o design em arquivos de *Migrations* seguras, aplicando travas contra perda de dados.

4. **Planejar as Tarefas (Task Planning)**
   - O **Arquiteto** decompõe a solução no checklist da Tarefa (em `docs/tasks/`).

5. **Desenvolver Testes Unitários (TDD)**
   - O **Tester** cria a suíte de testes (em código) antes de qualquer lógica produtiva.

6. **Executar (Execution)**
   - O **Desenvolvedor** programa focado em fazer os testes passarem em uma branch isolada da feature.

7. **Code Review (Manutenibilidade)**
   - O **Reviewer** inspeciona o código caçando falhas de Clean Code, complexidade cognitiva (SonarQube) e violações do Dicionário (`GLOSSARY.md`).

8. **Testar (Validation & QA)**
   - O **Tester** roda os testes automatizados e o plano de Auditoria manual para evitar regressões.

9. **Auditoria de Segurança (SecOps)**
   - O **Especialista de Segurança** varre o código aprovado atrás de vulnerabilidades e bloqueia se houver brechas (ex: Injections, LGPD).

10. **Release via Pull Request (DevOps)**
   - O **Engenheiro DevOps** configura os pipelines automáticos (CI/CD) e gera o PR da feature para a branch `develop`, com a descrição pré-preenchida. Commits diretos nas branches base são proibidos.

---

## Papéis dos Agentes

O **Orquestrador** não escreve código. Sua função é alternar entre os agentes e garantir que o `.agents/docs/STATE.md` esteja atualizado com o contexto atual.

- `.agents/orchestrator.md`
- `.agents/analyst.md`
- `.agents/architect.md`
- `.agents/designer.md`
- `.agents/dba.md`
- `.agents/developer.md`
- `.agents/reviewer.md`
- `.agents/tester.md`
- `.agents/security.md`
- `.agents/devops.md`
