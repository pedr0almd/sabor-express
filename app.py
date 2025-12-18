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
    '''
    Exibe o subtítulo 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(f'{linha} \n')
    
def voltar_para_o_inicio():
    '''
    Redireciona o usuário para o início do programa ao apertar qualquer tecla
    '''
    
    input('\nDigite QUALQUER tecla para voltar para o menu principal')
    main()

def exibir_nome_do_programa():
    '''
    Exibe o nome do programa no terminal
    '''
    print('Sabor Express')

def finalizar_app():
    '''
    Apenas exibe a mensagem de que o programa está sendo encerrado através da função 'exibir_subtitulo()'
    '''
    exibir_subtitulo('Encerrando o programa...')

def opcao_invalida():
    '''
    Mostar que a opção escolhida é invalida e redirecionar para o Inicio do programa
    
    Outputs:
    - Retorna ao menu
    '''
    print('Opção invalida!')
    voltar_para_o_inicio()
    
#------------------------------------
# Core
#------------------------------------

def cadastrar_restaurante():
    '''
    Essa função é responsável pelo cadastro de novos restaurantes
    
    Inputs:
    - Nome do Restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    
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
    '''
    Exibe uma lista de restaurantes com suas respectivas informações em formato de tabela
    
    Outputs:
    - Nome da função
    - Títulos da tabela
    - Informações de cada restaurante, divididos por linhas
    '''
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
    '''
    Altera o estado de um restaurate entre ativo e inativo
    
    Inputs:
    - Nome do restaurante
    
    Outputs:
    - Estado de sucesso
    - Retorna erro se o restaurante não for encontrado
    '''
    
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
    '''
    Exibe as opções da lista
    
    Outputs:
    - Opções da lista
    '''
    
    print('1) Cadastrar restaurante')
    print('2) Listar restaurante')
    print('3) Ativar/Desativar restaurante')
    print('4) Sair')

def escolher_opcao():
    '''
    Através da opção escolhida, executa uma função
    
    Inputs:
    - Número inteiro entre 1 e 4, com preveção de erro caso o usuário digite algo inesperado
    '''
    
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
    '''
    Função principal que inicializa o programa
    '''
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

#------------------------------------
# Execução
#------------------------------------    

if __name__ == '__main__':
    main()