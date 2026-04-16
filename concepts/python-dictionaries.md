# Dicionários (Python Dictionaries)

## O que é

Dicionários são uma das estruturas de dados mais versáteis do Python. Eles armazenam pares de **chave → valor**, permitindo acesso direto a qualquer elemento a partir de sua chave, sem precisar percorrer todos os itens como se faria em uma lista.

Diferente de listas (indexadas por posição numérica sequencial), dicionários permitem usar como chave qualquer valor imutável: inteiros, strings, tuplas, etc. Isso torna a busca por um elemento muito mais semântica e eficiente.

Dicionários também podem ser aninhados, ou seja, o valor de uma chave pode ser ele mesmo outro dicionário, formando estruturas hierárquicas de dados sem precisar de classes ou bancos de dados.

## Como é usado neste projeto

O projeto usa dois dicionários principais, ambos definidos no escopo global de `estoque.py`:

1. **`produtos`** — armazena o catálogo de produtos, usando o código numérico do produto como chave e um dicionário interno com `nome` e `quantidade` como valor.

2. **`historico_movimentacoes`** — tecnicamente é uma lista, mas cada item dentro dela é um dicionário com campos como `data`, `tipo`, `produto`, `quantidade_movimentada`, `responsavel`, etc.

O acesso ao estoque é feito diretamente por código: `produtos[codigo]['quantidade']`, sem nenhuma busca linear.

## Exemplo do projeto

```python
# Inicialização dos produtos
produtos = {
    1: {'nome': 'Bola', 'quantidade': 15},
    2: {'nome': 'Bicicleta', 'quantidade': 10},
    3: {'nome': 'Carrinho', 'quantidade': 20}
}

# Acesso e atualização via chave
produtos[codigo]['quantidade'] += quantidade
```

## Recursos para aprofundamento

- [Python Docs — Dicionários](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries) — documentação oficial em português
- [Real Python — Dictionaries in Python](https://realpython.com/python-dicts/) — guia completo com exemplos práticos
