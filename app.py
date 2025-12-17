import os

restaurantes = [
    {
     'nome': 'Praça', 
     'categoria': 'Japonesa',
     'ativo': False
     },
    
    {
     'nome': 'Pizza Suprema',
     'categoria': 'Pizza',
     'ativo': True
     },
    
    {
     'nome': 'Cantina',
     'categoria': 'Italiano',
     'ativo': False
     }
]

#-------------------------------------
# Utils
#-------------------------------------

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(f'{linha} \n')
    
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
    categoria_do_restaurante = input(f'Digite o nome da categoria dos restaurante: ')
    
    dados_do_restaurante = {
        'nome': nome_do_restaurante, 
        'categoria': categoria_do_restaurante,
        'ativo': 'False'
        }
    
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_para_o_inicio()

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')

    nome_tabela = f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)} |'
    print(nome_tabela)
    print('-' * len(nome_tabela))
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        estado_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo'
        
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {estado_restaurante.ljust(20)} |')
    
    voltar_para_o_inicio()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
        
            
    voltar_para_o_inicio()

#------------------------------------
# Menu
#------------------------------------

def exibir_opcoes():
    print('1) Cadastrar restaurante')
    print('2) Listar restaurante')
    print('3) Ativar/Desativar restaurante')
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
                alternar_estado_restaurante()
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