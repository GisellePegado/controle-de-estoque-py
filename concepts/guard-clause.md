# Retorno antecipado (Guard Clause - Early Return)

## O que é

Guard Clause (ou "retorno antecipado") é um padrão de programação onde condições de erro ou de cancelamento são tratadas logo no início de uma função, retornando imediatamente quando detectadas. Isso evita o aninhamento excessivo de `if/else` e deixa o código mais linear e legível.

O nome vem da ideia de que essas verificações iniciais são como "guardiões" que bloqueiam a execução principal caso algo não esteja em ordem. Em vez de escrever `if condicao_ok: faz_tudo_aqui`, escreve-se `if not condicao_ok: return` e o código principal segue sem indentação extra.

Em Python, é comum usar `None` como valor sentinela para indicar ausência ou cancelamento, em vez de usar exceções ou flags booleanas.

## Como é usado neste projeto

O projeto usa `None` como sinal de cancelamento em todas as funções de coleta de dados (`obter_codigo_produto`, `obter_tipo_movimentacao`, `obter_quantidade`, `validar_data`, `obter_responsavel`). Quando o usuário digita `0`, a função retorna `None`.

Na função `main()`, cada chamada é seguida de uma guard clause: se o retorno for `None`, imprime a mensagem de cancelamento e usa `continue` para voltar ao início do loop do menu, ignorando o restante do fluxo. Isso evita um `else` gigante que envolveria toda a lógica de movimentação.

## Exemplo do projeto

```python
# Sem guard clause — tudo aninhado:
codigo = obter_codigo_produto()
if codigo is not None:
    tipo = obter_tipo_movimentacao()
    if tipo is not None:
        # ... mais aninhamentos

# Com guard clause — fluxo linear:
codigo = obter_codigo_produto()
if codigo is None:
    print('\n✗ Operação cancelada.')
    continue

tipo = obter_tipo_movimentacao()
if tipo is None:
    print('\n✗ Operação cancelada.')
    continue
```

## Recursos para aprofundamento

- [Refactoring Guru — Replace Nested Conditional with Guard Clauses](https://refactoring.guru/replace-nested-conditional-with-guard-clauses) — explicação do padrão com exemplos
- [Martin Fowler — Guard Clauses](https://martinfowler.com/bliki/GuardClause.html) — origem e definição do padrão
