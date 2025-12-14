import os

restaurantes = ['Pizza', 'Lasanha']

#-------------------------------------
# Utils
#-------------------------------------

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('-' * 60)

def voltar_para_o_inicio():
    input('\nDigite QUALQUER tecla para voltar para o menu principal')
    main()

def exibir_nome_do_programa():
    print('Sabor Express')

def finalizar_app():
    exibir_subtitulo('Encerrando o programa...')

def opcao_invalida():
    print('Opção invalida!')
    voltar_para_o_inicio()
    
#------------------------------------
# Core
#------------------------------------

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_para_o_inicio()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')

    for restaurante in restaurantes:
        print(f'- {restaurante}')
    
    voltar_para_o_inicio()

def ativar_restaurante():
    exibir_subtitulo('Ativar restaurantes')

#------------------------------------
# Menu
#------------------------------------

def exibir_opcoes():
    print('1) Cadastrar restaurante')
    print('2) Listar restaurante')
    print('3) Ativar restaurante')
    print('4) Sair')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')
        match opcao_escolhida:
            case 1: 
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except: 
        opcao_invalida()

#------------------------------------
# Main
#------------------------------------

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

#------------------------------------
# Execução
#------------------------------------    

if __name__ == '__main__':
    main()