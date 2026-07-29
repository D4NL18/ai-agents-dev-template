# UI/UX: [Nome da Feature ou Entidade]

Este documento descreve as decisões específicas de Design e UX para esta funcionalidade. Ele estende e respeita os padrões definidos em `GLOBAL_PATTERNS.md`.

## 1. Descrição Visual
[Visão geral de como a interface desta funcionalidade será estruturada. Ex: Layout em Grid de 2 colunas, Modal de cadastro, Tabela centralizada.]

## 2. Componentes Específicos
[Listagem de componentes ou widgets que precisarão ser criados exclusivamente para esta interface]
- **Componente A:** [Descrição e comportamento esperado]
- **Componente B:** [Descrição, botões e ações internas]

## 3. Fluxo de Usuário (User Flow)
[A jornada do usuário nesta feature]
- **Acesso:** Como o usuário chega a esta tela.
- **Ações Principais:** O que o usuário tenta realizar aqui.
- **Feedback Esperado:** O que ocorre após o clique da ação principal (Ex: Fechar modal e atualizar tabela, redirecionamento para outra página).

## 4. Edge Cases Visuais (Tratamento de Exceções)
[Definições muito importantes para guiar o frontend nos cenários atípicos]
- **Empty State (Estado Vazio):** Como a tela se comporta se não houverem dados para mostrar? (Ex: Ilustração com botão "Criar novo").
- **Loading State:** Como a tela aguarda a API? (Ex: Skeleton, Spinner, bloqueio de inputs).
- **Tratamento de Erro de Integração:** Onde e como a mensagem de erro da API é exibida?
