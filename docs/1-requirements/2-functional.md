# Requisitos Funcionais (RFs)

## Introdução

Este documento cataloga os requisitos levantados a partir das histórias de usuário do Sistema de Controle de Estoque.

- **Requisitos Funcionais (RF):** descrevem o que o sistema deve fazer — as operações, comportamentos e funcionalidades que ele oferece ao usuário.

---

## Requisitos Funcionais

| ID   | Nome                                         | Descrição                                                                                                                                                   | Status          |
| ---- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| RF01 | Seleção de Produto Cadastrado                | O sistema deve permitir que o usuário busque e selecione produtos previamente cadastrados, exibindo código, nome e estoque atual.                           | ✅ Implementado |
| RF02 | Registro de Entrada de Produtos              | O sistema deve possibilitar o cadastro de entradas de produtos no estoque, permitindo informar a quantidade recebida e a data da entrada.                   | ✅ Implementado |
| RF03 | Atualização Automática do Estoque na Entrada | O sistema deve incrementar automaticamente a quantidade disponível em estoque após a confirmação da entrada.                                                | ✅ Implementado |
| RF04 | Registro de Saída de Produtos                | O sistema deve permitir o registro de saídas de produtos, com seleção do produto, quantidade retirada, data da movimentação e identificação do responsável. | ✅ Implementado |
| RF05 | Validação de Estoque Disponível              | O sistema deve validar se existe quantidade suficiente antes de confirmar uma saída, exibindo alerta e permitindo nova tentativa ou cancelamento.           | ✅ Implementado |
| RF06 | Histórico de Movimentações                   | O sistema deve manter um registro completo de todas as movimentações (entradas e saídas), armazenando data, tipo, quantidade, produto e responsável.        | ✅ Implementado |

### Detalhamento dos Requisitos

#### RF01 — Seleção de Produto Cadastrado

O sistema exibe a lista de produtos disponíveis com código, nome e quantidade atual ao iniciar uma movimentação. A função `obter_codigo_produto()` valida que o código digitado pertence ao dicionário `produtos` antes de prosseguir.

#### RF02 e RF03 — Registro e Atualização de Entrada

A função `realizar_entrada()` incrementa diretamente o campo `quantidade` do produto selecionado no dicionário `produtos` e registra a operação no histórico via `historico_movimentacoes.append()`.

#### RF04 — Registro de Saída

A função `realizar_saida()` captura os campos obrigatórios (produto, quantidade, data e responsável) e decrementa o estoque, registrando a movimentação com todos os dados exigidos.

#### RF05 — Validação de Estoque

A função `verificar_quantidade_disponivel()` compara a quantidade solicitada com o estoque atual. Em caso de insuficiência, `tratar_quantidade_insuficiente()` oferece ao usuário a opção de digitar outra quantidade ou cancelar a operação.

#### RF06 — Histórico de Movimentações

A lista global `historico_movimentacoes` acumula dicionários com os campos `data`, `tipo`, `produto`, `quantidade_movimentada`, `quantidade_anterior`, `quantidade_nova` e `responsavel`. A função `listar_movimentacoes()` exibe o histórico em formato de tabela tabulada no terminal.
