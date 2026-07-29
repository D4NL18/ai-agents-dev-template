# Padrão de Commits, Branches e Versionamento

O Desenvolvedor e toda a equipe devem seguir regras estritas de controle de versão.

## 1. Proteção de Branches (Bloqueio)
**É EXPRESSAMENTE PROIBIDO** para qualquer agente realizar commits diretos nas branches base: `develop`, `qa`, e `main`/`master`. Todo o desenvolvimento deve ocorrer isoladamente em novas branches.

## 2. Padrão de Branches
Cada tarefa planejada deve possuir uma branch isolada gerada a partir da `develop`.
- **Formato:** `tipo/P-XXX-descrição-curta`
- **Exemplos válidos:** `feature/P-001-valida-maioridade`, `fix/P-002-corrige-token`

## 3. Formato Obrigatório do Commit
O código dentro das branches isoladas deve seguir o modelo de **Conventional Commits**:
`<tipo>: [<referência>] <descrição no imperativo e em caixa baixa>`

### Tipos Permitidos
- `feat`: Uma nova funcionalidade ou regra implementada.
- `fix`: Correção de bug apontada pelo QA ou Segurança.
- `test`: Adição ou refatoração de testes (passo de TDD).
- `refactor`: Melhorias de clean code apontadas pelo Reviewer.
- `docs`: Atualizações de documentação (ex: atualizar o STATE.md).

### Exemplos Válidos de Commit
- `feat: [P-001] adiciona validação de maioridade na criação do cadastro`
- `refactor: [P-001] extrai lógicas de envio de email para serviço próprio`
