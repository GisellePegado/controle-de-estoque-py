# Input Validation

## O que é

Validação de entrada é o processo de verificar se os dados fornecidos pelo usuário (ou por qualquer fonte externa) atendem aos critérios esperados antes de usá-los no programa. É uma das práticas mais fundamentais de segurança e robustez em software.

Sem validação, um usuário que digita uma letra onde se espera um número pode causar erros inesperados, travar o programa ou até comprometer a integridade dos dados. Um programa robusto antecipa essas situações e guia o usuário a fornecer entradas corretas.

Em Python, a combinação de `try/except` com `while` é um padrão comum para validação: tenta-se converter ou usar a entrada; se der erro, informa o usuário e pede novamente.

## Como é usado neste projeto

O projeto aplica validação rigorosa em todos os pontos de entrada do usuário. As funções `obter_codigo_produto()`, `obter_tipo_movimentacao()` e `obter_quantidade()` usam o mesmo padrão: um loop `while` com `try/except ValueError` que só encerra quando o dado fornecido for válido.

Além de validar o tipo (inteiro vs. texto), o código valida também o **domínio** do valor — por exemplo, se o código existe no dicionário de produtos, se o tipo é 0, 1 ou 2, e se a quantidade não é negativa.

## Exemplo do projeto

```python
def obter_codigo_produto():
    """Solicita e valida o código do produto"""
    codigo_valido = False
    while not codigo_valido:
        try:
            codigo = int(input('\nDigite o código do produto (ou 0 para cancelar): '))
            if codigo in produtos or codigo == 0:
                codigo_valido = True
            else:
                print('Código inválido. Tente novamente\n')
        except ValueError:
            print('Entrada inválida. Digite apenas números.\n')
    
    return codigo if codigo != 0 else None
```

## Recursos para aprofundamento

- [Python Docs — Exceções](https://docs.python.org/pt-br/3/tutorial/errors.html) — como funciona o `try/except`
- [Real Python — Python Input Validation](https://realpython.com/python-input-integer/) — técnicas de validação de entrada
