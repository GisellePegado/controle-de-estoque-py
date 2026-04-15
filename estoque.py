from datetime import datetime

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

def validar_data():
    """Solicita e valida uma data no formato dd/mm/aaaa"""
    print('\n')
    print('=' * 50)
    print(' ' * 15 + 'DATA DA MOVIMENTAÇÃO')
    print('=' * 50)
    print('Formato: dd/mm/aaaa (ex: 04/12/2025)')
    print('=' * 50)
    
    data = input('\nDigite a data da movimentação (ou digite 0 para cancelar): ')
    
    if data == '0':
        return None
    
    data_valida = False
    
    while not data_valida:
        try:
            datetime.strptime(data, '%d/%m/%Y')
            data_valida = True
        except ValueError:
            print('Data inválida. Use o formato dd/mm/aaaa (ou digite 0 para cancelar)\n')
            data = input('Digite a data da movimentação: ')
            if data == '0':
                return None
    
    return data

def realizar_entrada(codigo, quantidade, data):
    """Registra entrada de produtos no estoque"""
    nome_produto = produtos[codigo]['nome']
    quantidade_anterior = produtos[codigo]['quantidade']
    produtos[codigo]['quantidade'] += quantidade
    quantidade_nova = produtos[codigo]['quantidade']
    
    # Registra no histórico
    historico_movimentacoes.append({
        'data': data,
        'tipo': 'Entrada',
        'produto': nome_produto,
        'quantidade_movimentada': quantidade,
        'quantidade_anterior': quantidade_anterior,
        'quantidade_nova': quantidade_nova,
        'responsavel': None
    })
    
    print(f'\n✓ {data}: Entrada de {quantidade} {nome_produto}(s) com sucesso!')

def verificar_quantidade_disponivel(codigo, quantidade):
    """Verifica se há quantidade suficiente em estoque"""
    return produtos[codigo]['quantidade'] >= quantidade

def realizar_saida(codigo, quantidade, data, responsavel):
    """Registra saída de produtos do estoque"""
    nome_produto = produtos[codigo]['nome']
    quantidade_anterior = produtos[codigo]['quantidade']
    produtos[codigo]['quantidade'] -= quantidade
    quantidade_nova = produtos[codigo]['quantidade']
    
    # Registra no histórico
    historico_movimentacoes.append({
        'data': data,
        'tipo': 'Saída',
        'produto': nome_produto,
        'quantidade_movimentada': quantidade,
        'quantidade_anterior': quantidade_anterior,
        'quantidade_nova': quantidade_nova,
        'responsavel': responsavel
    })
    
    print(f'\n✓ {data}: {responsavel} realizou retirada de {quantidade} {nome_produto}(s) com sucesso!')

def obter_responsavel():
    """Solicita o nome do responsável pela saída"""
    print('\n')
    print('=' * 50)
    print(' ' * 15 + 'RESPONSÁVEL')
    print('=' * 50)
    
    responsavel = input('\nDigite o nome do Responsável pela retirada (ou digite 0 para cancelar): ').strip()
    
    if responsavel == '0':
        return None
    
    while not responsavel:
        print('Nome do responsável não pode estar vazio.\n')
        responsavel = input('Digite o nome do Responsável pela retirada (ou 0 para cancelar): ').strip()
        if responsavel == '0':
            return None
    
    return responsavel

def realiza_movimentacao(codigo, tipo, quantidade, data, responsavel=None):
    """Realiza movimentação (entrada ou saída) de produtos"""
    if tipo == 1:  # Entrada
        realizar_entrada(codigo, quantidade, data)
    else:  # Saída
        realizar_saida(codigo, quantidade, data, responsavel)
    
    exibir_estoque()

def obter_codigo_produto():
    """Solicita e valida o código do produto"""
    print('\n')
    print('=' * 50)
    print(' ' * 12 + 'SELEÇÃO DE PRODUTO')
    print('=' * 50)
    for codigo, dados in produtos.items():
        print(f'{codigo} - {dados["nome"]} (Estoque: {dados["quantidade"]:02d})')
    print('=' * 50)
    
    codigo_valido = False
    while not codigo_valido:
        try:
            codigo = int(input('\nDigite o código do produto que deseja selecionar (ou digite 0 para cancelar): '))
            if codigo in produtos or codigo == 0:
                codigo_valido = True
            else:
                print('Código inválido. Tente novamente\n')
        except ValueError:
            print('Entrada inválida. Digite apenas números.\n')
    
    return codigo if codigo != 0 else None

def obter_tipo_movimentacao():
    """Solicita e valida o tipo de movimentação (entrada ou saída)"""
    print('\n')
    print('=' * 50)
    print(' ' * 10 + 'TIPO DE MOVIMENTAÇÃO')
    print('=' * 50)
    print('1 - Entrada no estoque')
    print('2 - Saída do estoque')
    print('=' * 50)
    
    tipo_valido = False
    while not tipo_valido:
        try:
            tipo = int(input('\nDigite o tipo de movimentação deseja registrar (ou digite 0 para cancelar): '))
            if tipo in [0, 1, 2]:
                tipo_valido = True
            else:
                print('Tipo de movimentação inválida. Tente novamente\n')
        except ValueError:
            print('Entrada inválida. Digite apenas números (0, 1 ou 2).\n')
    
    return tipo if tipo != 0 else None

def obter_quantidade():
    """Solicita e valida a quantidade a ser movimentada"""
    print('\n')
    print('=' * 50)
    print(' ' * 15 + 'QUANTIDADE')
    print('=' * 50)
    
    quantidade_valida = False
    while not quantidade_valida:
        try:
            quantidade = int(input('\nDigite a quantidade a ser movimentada (ou digite 0 para cancelar): '))
            if quantidade >= 0:
                quantidade_valida = True
            else:
                print('Quantidade inválida. Não pode ser negativa.\n')
        except ValueError:
            print('Entrada inválida. Digite apenas números.\n')
    
    return quantidade if quantidade != 0 else None

def tratar_quantidade_insuficiente(codigo, quantidade_solicitada):
    """Trata o caso de quantidade insuficiente no estoque"""
    nome_produto = produtos[codigo]['nome']
    quantidade_disponivel = produtos[codigo]['quantidade']
    
    print('\n')
    print('!' * 50)
    print(f'ERRO: Quantidade de {nome_produto}(s) insuficiente!')
    print(f'Quantidade solicitada: {quantidade_solicitada}')
    print(f'Quantidade disponível em estoque: {quantidade_disponivel:02d}')
    print('!' * 50)
    print('\nO que deseja fazer?')
    print('1 - Digitar outra quantidade')
    print('-' * 50)
    print('2 - Cancelar movimentação')
    print('=' * 50)
    
    opcao_valida = False
    while not opcao_valida:
        try:
            opcao = input('\nEscolha uma opção: ')
            if opcao in ['1', '2']:
                opcao_valida = True
            else:
                print('Opção inválida. Digite 1 ou 2.')
        except:
            print('Entrada inválida. Digite 1 ou 2.')
    
    if opcao == '1':
        # Retorna nova quantidade
        return obter_quantidade()
    else:
        # Retorna None para indicar cancelamento
        return None

def perguntar_continuar():
    """Pergunta se o usuário deseja continuar"""
    resposta = input('\nDeseja mais alguma coisa? (S/N): ').upper()
    while resposta != 'S' and resposta != 'N':
        print('Resposta inválida. Tente novamente\n')
        resposta = input('\nDeseja mais alguma coisa? (S/N): ').upper()
    return resposta == 'S'

def listar_movimentacoes():
    """Lista todas as movimentações realizadas em formato de tabela"""
    if not historico_movimentacoes:
        print('\nNenhuma movimentação registrada ainda.')
        return
    
    print('\n')
    print('=' * 120)
    print(' ' * 45 + 'HISTÓRICO DE MOVIMENTAÇÕES')
    print('=' * 120)
    
    # Cabeçalho da tabela
    print(f'{"#":<4} | {"Data":<10} | {"Tipo":<8} | {"Produto":<12} | {"Qtd Mov":<8} | {"Qtd Ant":<8} | {"Qtd Nova":<8} | {"Responsável":<20}')
    print('-' * 120)
    
    # Linhas da tabela
    for i, mov in enumerate(historico_movimentacoes, 1):
        responsavel = mov["responsavel"] if mov["responsavel"] else "-"
        print(f'{i:<4} | {mov["data"]:<10} | {mov["tipo"]:<8} | {mov["produto"]:<12} | '
              f'{mov["quantidade_movimentada"]:<8} | {mov["quantidade_anterior"]:02d}       | '
              f'{mov["quantidade_nova"]:02d}       | {responsavel:<20}')
    
    print('=' * 120)
    print(f'Total de movimentações: {len(historico_movimentacoes)}')
    print('=' * 120)

def exibir_menu():
    """Exibe o menu principal"""
    print('\n')
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

# Programa principal
def main():
    """Função principal do sistema de estoque"""
    print('Bem vindo ao Sistema de Estoque da Giselle maria Ferreira Pegado da Silva!')
    exibir_estoque()
    
    continuar = True
    
    while continuar:
        opcao = exibir_menu()
        
        if opcao == '0':  # Sair
            continuar = False
            print('\nObrigado por usar o Sistema de Estoque!')
        
        elif opcao == '1':  # Realizar movimentação
            codigo = obter_codigo_produto()
            if codigo is None:
                print('\n✗ Operação cancelada.')
                continue
            
            tipo = obter_tipo_movimentacao()
            if tipo is None:
                print('\n✗ Operação cancelada.')
                continue
            
            quantidade = obter_quantidade()
            if quantidade is None:
                print('\n✗ Operação cancelada.')
                continue
            
            # Se for saída, verifica primeiro se há quantidade suficiente
            if tipo == 2:  # Saída
                # Loop para tratar quantidade insuficiente
                while not verificar_quantidade_disponivel(codigo, quantidade):
                    quantidade = tratar_quantidade_insuficiente(codigo, quantidade)
                    
                    # Se retornou None, usuário cancelou a movimentação
                    if quantidade is None:
                        print('\n✗ Movimentação cancelada.')
                        break
                
                # Se não cancelou, continua com a movimentação
                if quantidade is not None:
                    responsavel = obter_responsavel()
                    if responsavel is None:
                        print('\n✗ Operação cancelada.')
                        continue
                    
                    data = validar_data()
                    if data is None:
                        print('\n✗ Operação cancelada.')
                        continue
                    
                    realiza_movimentacao(codigo, tipo, quantidade, data, responsavel)
            else:  # Entrada
                data = validar_data()
                if data is None:
                    print('\n✗ Operação cancelada.')
                    continue
                
                realiza_movimentacao(codigo, tipo, quantidade, data)
        
        elif opcao == '2':  # Listar histórico
            listar_movimentacoes()
        
        elif opcao == '3':  # Exibir estoque
            exibir_estoque()

if __name__ == '__main__':
    main()
