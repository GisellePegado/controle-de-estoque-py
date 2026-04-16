# CLI Menu Pattern

## O que é

CLI (*Command-Line Interface*) é um estilo de interface em que o usuário interage com o programa digitando comandos ou escolhas em um terminal de texto, em vez de clicar em elementos visuais. É a forma mais fundamental de criar interfaces interativas em Python sem depender de bibliotecas externas de GUI ou frameworks web.

O padrão de menu em CLI funciona com um loop principal que exibe as opções disponíveis, lê a escolha do usuário e executa a ação correspondente. O loop continua até que o usuário escolha sair. É simples, portável e suficiente para muitos sistemas internos, ferramentas de automação e projetos acadêmicos.

## Como é usado neste projeto

O sistema inteiro é construído em torno de um menu CLI. A função `exibir_menu()` imprime as opções formatadas com bordas de caracteres ASCII (`=`, `-`) e retorna a opção escolhida após validação. O loop principal em `main()` lê essa opção e despacha para a função correta.

O projeto também utiliza menus secundários (como o de tipo de movimentação e o de tratamento de quantidade insuficiente), todos seguindo o mesmo padrão de loop com validação.

## Exemplo do projeto

```python
def exibir_menu():
    """Exibe o menu principal"""
    print('=' * 50)
    print(' ' * 15 + 'MENU PRINCIPAL')
    print('=' * 50)
    print('1 - Realizar movimentação (Entrada/Saída)')
    print('2 - Listar histórico de movimentações')
    print('3 - Exibir estoque atual')
    print('-' * 50)
    print('0 - Sair do sistema')
    print('=' * 50)
    
    opcao = input('\nEscolha uma opção: ')
    while opcao not in ['0', '1', '2', '3']:
        print('Opção inválida. Tente novamente.')
        opcao = input('Escolha uma opção: ')
    
    return opcao
```

## Recursos para aprofundamento

- [Real Python — Build a CLI with Python](https://realpython.com/command-line-interfaces-python-argparse/) — introdução a CLIs em Python
- [Python Docs — input()](https://docs.python.org/pt-br/3/library/functions.html#input) — função de leitura de entrada do usuário
