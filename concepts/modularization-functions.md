# Modularização com Funções (Modularization with Functions)

## O que é

Modularização é o princípio de dividir um programa em partes menores, independentes e reutilizáveis — chamadas funções, módulos ou classes, dependendo da linguagem e do nível de abstração. Cada parte resolve um problema específico e bem delimitado.

Programas não modularizados tendem a crescer em um único bloco monolítico, tornando difícil entender, testar e modificar o código. A modularização combate esse problema ao criar **fronteiras claras de responsabilidade**: cada função sabe o que faz e não precisa saber como as outras funcionam internamente.

Em Python, a unidade básica de modularização é a função (`def`), que pode receber parâmetros, executar lógica e retornar valores. Quando o projeto cresce, funções são agrupadas em módulos (arquivos `.py`) e depois em pacotes (pastas com `__init__.py`).

## Como é usado neste projeto

O arquivo `estoque.py` é inteiramente estruturado em funções — não há lógica solta fora delas (exceto inicializações globais). Cada operação do sistema tem sua própria função com nome descritivo:

- `exibir_estoque()` — renderiza a tabela de estoque
- `validar_data()` — lida exclusivamente com a entrada e validação da data
- `realizar_entrada()` / `realizar_saida()` — registram a movimentação no estoque e no histórico
- `obter_codigo_produto()` / `obter_tipo_movimentacao()` / `obter_quantidade()` — coletam dados do usuário
- `listar_movimentacoes()` — exibe o histórico formatado
- `main()` — orquestra o fluxo geral do programa

A função `main()` fica limpa e legível porque toda a complexidade está encapsulada nas funções auxiliares.

## Exemplo do projeto

```python
def realiza_movimentacao(codigo, tipo, quantidade, data, responsavel=None):
    """Realiza movimentação (entrada ou saída) de produtos"""
    if tipo == 1:  # Entrada
        realizar_entrada(codigo, quantidade, data)
    else:  # Saída
        realizar_saida(codigo, quantidade, data, responsavel)
    
    exibir_estoque()
```

## Recursos para aprofundamento

- [Python Docs — Funções](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions) — referência oficial
- [Real Python — Python Functions](https://realpython.com/defining-your-own-python-function/) — guia prático de funções em Python
