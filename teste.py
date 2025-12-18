import os

pessoas = [{
    'nome': 'Pedro',
    'idade': '19',
    'cidade': 'São Paulo',
    'profissao': 'Estagiario TI'
}]

def adicionar_pessoa():
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    cidade = input('Digite a cidade: ')
    profissao = input('Digite a profissao: ')
    
    dados_da_pessoa = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade,
        'profissao': profissao
    }
    
    pessoas.append(dados_da_pessoa)
    print(pessoas)
    
def remover_pessoa():
    pass

def atualizar_dados_pessoa():
    pass

def mostrar_opcoes():
    pass

def escolher_opcoes():
    pass

def main():
    adicionar_pessoa()

if __name__ == '__main__':
    main()