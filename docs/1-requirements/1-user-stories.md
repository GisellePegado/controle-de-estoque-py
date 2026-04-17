# Histórias de Usuário

## Introdução

Este documento descreve as histórias de usuário que orientaram o desenvolvimento do Sistema de Controle de Estoque. As histórias foram elaboradas na disciplina de Engenharia de Software e seguem o formato padrão de user stories, acompanhadas de critérios de aceitação que definem quando cada funcionalidade pode ser considerada implementada com sucesso.

Cada história representa uma necessidade real de um funcionário do almoxarifado, descrita do ponto de vista de quem utiliza o sistema — sem detalhes técnicos de implementação, focando no valor entregue.

---

## HU-01 — Entrada de Produto no Estoque

**Como** funcionário do setor de almoxarifado,  
**quero** registrar a entrada de produtos no estoque,  
**para que** o sistema reflita corretamente os itens disponíveis após uma nova entrega ou compra.

### Critérios de Aceitação

- O sistema deve permitir selecionar um produto já cadastrado.
- Deve ser possível informar a quantidade recebida e a data da entrada.
- O estoque do produto deve ser atualizado automaticamente após a confirmação.

### Implementação no Código

| Critério | Função responsável |
|----------|-------------------|
| Selecionar produto cadastrado | `obter_codigo_produto()` |
| Informar quantidade | `obter_quantidade()` |
| Informar data da entrada | `validar_data()` |
| Atualizar estoque automaticamente | `realizar_entrada()` |

---

## HU-02 — Saída de Produto do Estoque

**Como** funcionário do almoxarifado,  
**quero** registrar a saída de produtos do estoque,  
**para que** o controle dos itens utilizados ou entregues seja mantido com precisão.

### Critérios de Aceitação

- O sistema deve permitir selecionar um produto e informar a quantidade retirada.
- Deve validar se há quantidade suficiente no estoque antes de confirmar a saída.
- O sistema deve registrar a movimentação com data e responsável pela retirada.

### Implementação no Código

| Critério | Função responsável |
|----------|-------------------|
| Selecionar produto e quantidade | `obter_codigo_produto()`, `obter_quantidade()` |
| Validar estoque disponível | `verificar_quantidade_disponivel()` |
| Registrar data e responsável | `validar_data()`, `obter_responsavel()` |
| Persistir a saída no histórico | `realizar_saida()` |
