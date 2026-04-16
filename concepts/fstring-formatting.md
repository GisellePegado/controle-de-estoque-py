# Formatação com f-strings (f-string Formatting)

## O que é

F-strings (ou *formatted string literals*) são uma forma moderna e eficiente de embutir expressões Python diretamente dentro de strings, usando o prefixo `f` e chaves `{}`. Introduzidas no Python 3.6, elas substituem métodos mais antigos como `%` e `.format()` com uma sintaxe mais legível e mais rápida.

Além de inserir variáveis, as f-strings suportam **especificadores de formato** dentro das chaves, como `{valor:02d}` (inteiro com zero à esquerda e mínimo 2 dígitos) ou `{texto:<12}` (texto alinhado à esquerda com largura fixa de 12 caracteres). Esses especificadores são especialmente úteis para exibir dados em formato de tabela no terminal.

## Como é usado neste projeto

O projeto usa f-strings extensivamente para construir as saídas formatadas no terminal — tabelas de estoque, histórico de movimentações e mensagens de confirmação. Os especificadores de formato garantem que os valores fiquem alinhados corretamente nas colunas:

- `{dados["nome"]:<11}` — nome alinhado à esquerda em 11 caracteres
- `{dados["quantidade"]:02d}` — quantidade com zero à esquerda (ex: `05`)
- `{mov["tipo"]:<8}` — tipo da movimentação com largura fixa de 8

## Exemplo do projeto

```python
# Tabela de estoque com alinhamento de colunas
for codigo, dados in produtos.items():
    print(f'|   {codigo}    |   {dados["nome"]:<11} |      {dados["quantidade"]:02d}      |')

# Tabela de histórico com múltiplos especificadores
print(f'{i:<4} | {mov["data"]:<10} | {mov["tipo"]:<8} | {mov["produto"]:<12} | '
      f'{mov["quantidade_movimentada"]:<8} | {mov["quantidade_anterior"]:02d}       | '
      f'{mov["quantidade_nova"]:02d}       | {responsavel:<20}')

# Mensagem de confirmação com dados dinâmicos
print(f'\n✓ {data}: Entrada de {quantidade} {nome_produto}(s) com sucesso!')
```

## Recursos para aprofundamento

- [Python Docs — f-strings](https://docs.python.org/pt-br/3/reference/lexical_analysis.html#formatted-string-literals) — referência oficial
- [Real Python — Python f-Strings](https://realpython.com/python-f-strings/) — guia completo com exemplos de especificadores
- [Python Format Spec Mini-Language](https://docs.python.org/3/library/string.html#format-specification-mini-language) — referência de todos os especificadores de formato
