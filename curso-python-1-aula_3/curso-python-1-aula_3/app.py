import os

# restaurantes = ['Pizza', 'Sushi']
restaurantes = [
    {'nome': 'Praça', 'categoria':'Japonesa', 'ativo':False},
    {'nome': 'Pizza Suprema', 'categoria':'Italiana', 'ativo':True},
    {'nome': 'Cantina', 'categoria':'Italiana', 'ativo':False}
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    print('\033[H\033[J', end='')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(f'{linha} \n\n\n')

def cadastrar_novo_restaurante():
    '''
        Função responsável por cadastrar um novo restaurante.
        Input: 
           - nome do restaurante
           - categoria.

        Output:
            - mensagem de sucesso

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')     
    
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterar estado do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_do_restaurante.lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo']:
                mensagem = f'O restaurante {restaurante["nome"]} foi ativado com sucesso!' 
            else:
                mensagem = f'O restaurante {restaurante["nome"]} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado!')    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(24) } | {'Categoria'.ljust(24)} | {'Status'.ljust(24)}')    
    print ('-'*24 + ' | ' + '-'*24 + ' | ' + '-'*24)

    for restaurante in restaurantes:
        ativo =  'Ativado' if restaurante['ativo'] else 'Desativado'
        # print(f'{restaurante['nome']} \t\t | {restaurante['categoria']} \t\t | {ativo}')
        print(f'{restaurante['nome'].ljust(24)} | {restaurante['categoria'].ljust(24)} | {ativo}')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    print('\033[H\033[J', end='')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()