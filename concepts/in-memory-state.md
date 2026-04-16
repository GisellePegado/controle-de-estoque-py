# Gerenciamento de estado em Memória (In-Memory State Management)

## O que é

Gerenciamento de estado em memória significa manter os dados da aplicação em variáveis (listas, dicionários, objetos) durante a execução do programa, sem persistir nada em disco ou banco de dados. Os dados existem apenas enquanto o programa está rodando; ao encerrar, tudo é perdido.

Essa abordagem é simples e adequada para protótipos, sistemas de estudo, ferramentas de uso imediato ou situações em que a persistência não é necessária. Quando a persistência se torna um requisito, o próximo passo natural é introduzir um arquivo (JSON, CSV) ou um banco de dados (SQLite, PostgreSQL).

Em Python, o estado em memória é tipicamente mantido em variáveis globais ou em objetos passados entre funções.

## Como é usado neste projeto

O projeto mantém dois estados globais em `estoque.py`:

1. **`produtos`** (dicionário) — representa o estado atual do estoque. É modificado diretamente pelas funções `realizar_entrada()` e `realizar_saida()` toda vez que uma movimentação ocorre.

2. **`historico_movimentacoes`** (lista) — acumula um registro de cada movimentação realizada durante a sessão. Cada `append()` adiciona um novo evento ao histórico, que é exibido pela função `listar_movimentacoes()`.

Ao reiniciar o programa, o estoque volta ao estado inicial definido no código (Bola: 15, Bicicleta: 10, Carrinho: 20) e o histórico fica vazio.

## Exemplo do projeto

```python
# Estado global — persiste durante toda a execução
produtos = {
    1: {'nome': 'Bola', 'quantidade': 15},
    ...
}
historico_movimentacoes = []

def realizar_entrada(codigo, quantidade, data):
    produtos[codigo]['quantidade'] += quantidade   # muta o estado
    historico_movimentacoes.append({               # adiciona ao histórico
        'data': data,
        'tipo': 'Entrada',
        ...
    })
```

## Recursos para aprofundamento

- [Real Python — Python Global Variables](https://realpython.com/python-scope-legb-rule/) — escopo e variáveis globais em Python
- [Python Docs — list.append](https://docs.python.org/pt-br/3/tutorial/datastructures.html) — listas e seus métodos
