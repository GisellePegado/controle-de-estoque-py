# Registro de Eventos / Histórico (Event Log)

## O que é

Um Event Log (ou Registro de Eventos) é uma estrutura que acumula de forma cronológica e imutável cada ação relevante que ocorreu no sistema. Em vez de apenas atualizar o estado atual, o programa também registra *o que aconteceu*, *quando* e *quem* foi o responsável.

Esse padrão é fundamental em sistemas de negócios onde rastreabilidade importa: vendas, movimentações de estoque, transações financeiras. A lista de eventos serve como uma "trilha de auditoria" que permite reconstruir o histórico completo, identificar erros e entender como o sistema chegou ao estado atual.

## Como é usado neste projeto

O projeto mantém a lista global `historico_movimentacoes` em `estoque.py`. A cada entrada ou saída realizada, as funções `realizar_entrada()` e `realizar_saida()` fazem um `append()` adicionando um dicionário com todos os detalhes da movimentação: data, tipo, produto, quantidade anterior, quantidade nova e responsável.

A função `listar_movimentacoes()` percorre essa lista e a exibe em formato de tabela, mostrando inclusive a quantidade antes e depois de cada operação — o que torna possível rastrear exatamente como o estoque evoluiu.

## Exemplo do projeto

```python
# Lista global que acumula os eventos
historico_movimentacoes = []

def realizar_saida(codigo, quantidade, data, responsavel):
    nome_produto = produtos[codigo]['nome']
    quantidade_anterior = produtos[codigo]['quantidade']
    produtos[codigo]['quantidade'] -= quantidade
    quantidade_nova = produtos[codigo]['quantidade']

    # Registra o evento no histórico com todos os detalhes
    historico_movimentacoes.append({
        'data': data,
        'tipo': 'Saída',
        'produto': nome_produto,
        'quantidade_movimentada': quantidade,
        'quantidade_anterior': quantidade_anterior,
        'quantidade_nova': quantidade_nova,
        'responsavel': responsavel
    })
```

## Recursos para aprofundamento

- [Martin Fowler — Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) — padrão arquitetural baseado em eventos
- [Python Docs — list.append](https://docs.python.org/pt-br/3/tutorial/datastructures.html) — listas e como acrescentar elementos
