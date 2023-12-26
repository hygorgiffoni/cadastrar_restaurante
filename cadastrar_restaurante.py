'Módulo para habilitar opções de cadastrar e ativar restaurantes no aplicativo Sabor Express.'
import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome():
    '''Exibe o nome do programa'''
    linha = '*' * (len('      SABOR EXPRESS      '))
    print(linha)
    print('      SABOR EXPRESS      ')
    print(linha)

def exibir_opcoes():
    '''Exibe as opções do programa'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Finaliza o aplicativo'''
    exibir_subtitulo('Finalizando o app')

def retorna_menu_principal():
    '''Retorna para o menu principal'''
    input('\nAperte enter para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Retorna um alerta que opção escolhida é inválida'''
    print('Opção inválida!')
    retorna_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe o subtitulo cadastrado'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(f'{texto}')
    print(linha)

def cadastrar_restaurante():
    '''Cadastra um novo restaurante'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    retorna_menu_principal()

def listar_restaurantes():
    '''Lista todos os restaurantes cadastrados'''
    exibir_subtitulo('Listando todos os restaurantes cadastrados')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    retorna_menu_principal()

def status_restaurante():
    '''Alterna o status do restaurante para ativo ou inativo'''
    exibir_subtitulo('Alternando o status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem_ativo = f'O restaurante {nome_restaurante} foi ativado com sucesso'
            mensagem_inativo = f'O restaurante {nome_restaurante} foi desativado com sucesso'
            mensagem = mensagem_ativo if restaurante['ativo'] else mensagem_inativo
            print(mensagem) # Sem efeito.
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    retorna_menu_principal()

def escolher_opcao():
    '''Escolhe opção do menu'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    '''Executa o programa'''
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
