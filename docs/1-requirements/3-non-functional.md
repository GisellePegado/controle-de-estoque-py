# Requisitos Não Funcionais (RNFs)

## Introdução

Este documento cataloga os requisitos levantados a partir das histórias de usuário do Sistema de Controle de Estoque.

- **Requisitos Não Funcionais (RNF):** descrevem como o sistema deve se comportar — restrições de qualidade como desempenho, segurança, usabilidade e manutenibilidade.

A coluna **Status** indica se o requisito foi implementado na versão atual do sistema (`estoque.py`). Requisitos marcados como `⚠️ Parcial` foram atendidos dentro das limitações de uma aplicação CLI sem banco de dados persistente.

---

## Requisitos Não Funcionais

| ID    | Nome             | Descrição                                                                                                                            | Status      |
| ----- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| RNF01 | Desempenho       | O sistema deve processar e confirmar operações de entrada e saída em no máximo 3 segundos.                                           | ✅ Atendido |
| RNF02 | Usabilidade      | A interface deve ser intuitiva, permitindo que funcionários com conhecimento básico em informática operem sem treinamento extensivo. | ✅ Atendido |
| RNF03 | Segurança        | O sistema deve implementar controle de acesso por perfis e registrar log de todas as ações para rastreabilidade.                     | ⚠️ Parcial  |
| RNF04 | Confiabilidade   | O sistema deve garantir integridade dos dados com transações atômicas e disponibilidade mínima de 99% em horário comercial.          | ⚠️ Parcial  |
| RNF05 | Manutenibilidade | O código deve seguir boas práticas, incluindo documentação adequada, padrões de projeto e arquitetura modular.                       | ✅ Atendido |
| RNF06 | Compatibilidade  | O sistema deve ser compatível com os principais navegadores e responsivo para desktop e tablets.                                     | ⚠️ N/A      |

### Observações

**RNF01 — Desempenho:** Como todas as operações ocorrem em memória (sem acesso a banco de dados ou rede), o tempo de resposta é imperceptível ao usuário.

**RNF02 — Usabilidade:** O sistema apresenta menus claros com opções numeradas, mensagens de erro descritivas e confirmações de cada operação realizada. O fluxo é guiado passo a passo, reduzindo a margem de erro do usuário.

**RNF03 — Segurança:** O histórico de movimentações registra todas as ações com responsável (para saídas), atendendo parcialmente o requisito de rastreabilidade. Controle de acesso por perfis não foi implementado nesta versão CLI.

**RNF04 — Confiabilidade:** A versão atual mantém os dados em memória durante a sessão. Não há persistência entre execuções nem mecanismo de backup, o que limita o atendimento pleno deste requisito.

**RNF05 — Manutenibilidade:** O código segue o princípio de responsabilidade única — cada função realiza exatamente uma tarefa, com nomes descritivos e docstrings. A pasta `concepts/` complementa a documentação técnica do projeto.

**RNF06 — Compatibilidade:** Requisito não aplicável nesta versão, pois o sistema é executado via terminal (CLI), sem interface web ou mobile.
