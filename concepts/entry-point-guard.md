# Ponto de Entrada com __name__ (Entry Point Guard)

## O que é

Em Python, todo arquivo `.py` é considerado um módulo. Quando um arquivo é executado diretamente pelo interpretador, a variável especial `__name__` recebe o valor `'__main__'`. Quando esse mesmo arquivo é importado por outro módulo, `__name__` recebe o nome do módulo (ex: `'estoque'`).

O padrão `if __name__ == '__main__':` é uma guarda que garante que determinado código só execute quando o arquivo é o ponto de entrada do programa — e não quando é importado como biblioteca. É uma convenção universal em Python e sinaliza claramente onde a execução do programa começa.

## Como é usado neste projeto

No arquivo `estoque.py`, toda a lógica de interação com o usuário está encapsulada na função `main()`. O bloco `if __name__ == '__main__':` no final do arquivo chama `main()` apenas quando `estoque.py` é executado diretamente.

Isso significa que, se no futuro alguém quiser importar funções de `estoque.py` em outro módulo (por exemplo, para testes ou para reutilizar `exibir_estoque()`), o menu interativo não será ativado automaticamente.

## Exemplo do projeto

```python
def main():
    """Função principal do sistema de estoque"""
    print('Bem vindo ao Sistema de Estoque da Giselle maria Ferreira Pegado da Silva!')
    exibir_estoque()
    
    continuar = True
    while continuar:
        opcao = exibir_menu()
        # ... lógica do menu

# Só executa se este arquivo for o ponto de entrada
if __name__ == '__main__':
    main()
```

## Recursos para aprofundamento

- [Python Docs — __main__](https://docs.python.org/pt-br/3/library/__main__.html) — documentação oficial do módulo `__main__`
- [Real Python — if __name__ == "__main__"](https://realpython.com/if-name-main-python/) — explicação detalhada do padrão e seus usos
