# Inicialização dos produtos
produtos = {
    1: {'nome': 'Bola', 'quantidade': 15},
    2: {'nome': 'Bicicleta', 'quantidade': 10},
    3: {'nome': 'Carrinho', 'quantidade': 20}
}

# Lista para armazenar todas as movimentações
historico_movimentacoes = []

def exibir_estoque():
    """Exibe o estoque atual de todos os produtos"""
    print('\n')
    print('-' * 16, 'Estoque', '-' * 16)
    print('-' * 41)
    print('| Código','|    Nome       |  Quantidade  |')
    print('-' * 41)
    for codigo, dados in produtos.items():
        print(f'|   {codigo}    |   {dados["nome"]:<11} |      {dados["quantidade"]:02d}      |')
    print('-' * 41)

def exibir_menu_generico(titulo, opcoes=None, mensagem_input='Escolha uma opção'):
    """Exibe um menu formatado e retorna a entrada do usuário"""
    print('\n')
    print('=' * 50)
    print(f'{titulo.upper():^50}')  # Centraliza o título
    print('=' * 50)
    
    if opcoes:
        for opcao in opcoes:
            print(opcao)
        print('=' * 50)
    
    return input(f'\n{mensagem_input}: ')

def registrar_no_historico(data, tipo, nome_produto, quantidade, quantidade_anterior, quantidade_nova, responsavel=None):
    historico_movimentacoes.append({
        'data': data,
        'tipo': tipo,
        'produto': nome_produto,
        'quantidade_movimentada': quantidade,
        'quantidade_anterior': quantidade_anterior,
        'quantidade_nova': quantidade_nova,
        'responsavel': responsavel
    })

def realizar_movimentacao(codigo, tipo, quantidade, data, responsavel=None):
    """Realiza movimentação (entrada ou saída) de produtos"""
    if tipo == 1:  # Entrada
        realizar_entrada(codigo, quantidade, data)
    else:  # Saída
        realizar_saida(codigo, quantidade, data, responsavel)
    return True

def realizar_entrada(codigo, quantidade, data):
    """Registra entrada de produtos no estoque"""
    nome_produto = produtos[codigo]['nome']
    quantidade_anterior = produtos[codigo]['quantidade']
    produtos[codigo]['quantidade'] += quantidade
    quantidade_nova = produtos[codigo]['quantidade']
    
    registrar_no_historico(data, 'Entrada', nome_produto, quantidade, quantidade_anterior, quantidade_nova)
    
    print(f'\n{data}: Entrada de {quantidade} {nome_produto.lower()}(s) com sucesso!')

def realizar_saida(codigo, quantidade, data, responsavel):
    """Registra saída de produtos do estoque"""
    nome_produto = produtos[codigo]['nome']
    quantidade_anterior = produtos[codigo]['quantidade']
    produtos[codigo]['quantidade'] -= quantidade
    quantidade_nova = produtos[codigo]['quantidade']
    
    registrar_no_historico(data, 'Saída', nome_produto, quantidade, quantidade_anterior, quantidade_nova, responsavel)
    
    print(f'\n{data}: {responsavel} realizou retirada de {quantidade} {nome_produto.lower()}(s) com sucesso!')

def obter_codigo_produto():
    """Solicita o código do produto"""
    opcoes = []
    return int(exibir_menu_generico('Seleção do Produto', opcoes, 
                                     'Digite o código do produto que deseja selecionar (ou digite 0 para sair)'))

def obter_tipo_movimentacao():
    """Solicita o tipo de movimentação (entrada ou saída)"""
    opcoes = [
        '1 - Entrada no estoque',
        '2 - Saída do estoque'
    ]
    return int(exibir_menu_generico('Tipo de Movimentação', opcoes, 
                                     'Digite o tipo de movimentação desejada'))

def obter_quantidade(nome_produto, tipo):
    """Solicita a quantidade a ser movimentada"""
    if tipo == 2:
        acao = "retirada"
        conector = "do"
    else:
        acao = "incluída"
        conector = "no"
    return int(exibir_menu_generico(f'Quantidade de {nome_produto}s {acao}', None, 
                                     f'Digite a quantidade de {nome_produto.lower()}s {acao} {conector} estoque'))


def obter_data(nome_produto, tipo):
    """Solicita uma data no formato dd/mm/aaaa"""
    subst = "inclusão" if tipo == 1 else "retirada"
    opcoes = ['Formato: dd/mm/aaaa (ex: 04/12/2025)']
    return exibir_menu_generico(f'Data de {subst}', opcoes, 
                                f'Digite a data de {subst} de {nome_produto.lower()}(s)')

def obter_responsavel():
    """Solicita o nome do responsável pela saída"""
    return exibir_menu_generico('Responsável pela retirada', None, 
                                'Digite o nome do Responsável pela retirada')

def listar_movimentacoes():
    """Lista todas as movimentações realizadas em formato de tabela"""
    if not historico_movimentacoes:
        print('\nNenhuma movimentação registrada ainda.')
        return
    
    print('\n')
    print('=' * 95)
    print(' ' * 30 + 'HISTÓRICO DE MOVIMENTAÇÕES')
    print('=' * 95)
    
    # Cabeçalho da tabela
    print(f'{"#":<4} | {"Data":<10} | {"Tipo":<8} | {"Produto":<12} | {"Qtd Mov":<8} | {"Qtd Ant":<8} | {"Qtd Nova":<8} | {"Responsável":<20}')
    print('-' * 95)
    
    # Linhas da tabela
    for i, mov in enumerate(historico_movimentacoes, 1):
        responsavel = mov["responsavel"] if mov["responsavel"] else "-"
        print(f'{i:<4} | {mov["data"]:<10} | {mov["tipo"]:<8} | {mov["produto"]:<12} | '
              f'{mov["quantidade_movimentada"]:<8} | {mov["quantidade_anterior"]:02d}       | '
              f'{mov["quantidade_nova"]:02d}       | {responsavel:<20}')
    
    print('=' * 95)
    print(f'Total de movimentações: {len(historico_movimentacoes)}')
    print('=' * 95)


# Programa principal
def main():
    """Função principal do sistema de estoque"""
    print('Bem vindo ao Sistema de Estoque da \033[35;1mGiselle Maria Ferreira Pegado da Silva\033[0m!')

    
    continuar = True
    
    while continuar:
        exibir_estoque()
        codigo = obter_codigo_produto()
        if codigo == 0:
            print('\nObrigado por usar o Sistema de Estoque!')
            break
        tipo = obter_tipo_movimentacao()
        nome_produto = produtos[codigo]['nome']
        quantidade = obter_quantidade(nome_produto, tipo)
            
        # Inicializa responsavel como None (para entradas)
        responsavel = None
        prosseguir = True
            
        # Se for saída, valida quantidade e pede responsável
        if tipo == 2:
            if produtos[codigo]['quantidade'] < quantidade:
                quantidade_disponivel = produtos[codigo]['quantidade']
                print('\n')
                print('-' * 50)
                print(f'ERRO: Quantidade de {nome_produto.lower()}s insuficiente!')
                print(f'Quantidade solicitada: {quantidade}')
                print(f'Quantidade disponível em estoque: {quantidade_disponivel:02d}')
                print('-' * 50)
                prosseguir = False
            else:
                responsavel = obter_responsavel()
            
        # Se passou nas validações, pede data e realiza movimentação
        if prosseguir:
            data = obter_data(nome_produto, tipo)
            realizar_movimentacao(codigo, tipo, quantidade, data, responsavel)
            listar_movimentacoes()

if __name__ == '__main__':
    main()
