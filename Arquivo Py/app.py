from classes import *
print('Bem vindo ao Gerenciador de Biblioteca!')
continuacao = 'y'
nome_da_bib = input('Digite o nome da sua biblioteca: ')
biblioteca = Biblioteca(nome_da_bib)
print('='*50)
while continuacao.lower() == 'y':
    print('''
O que você deseja fazer? 

1) Adicionar livro
2) Adicionar membro
3) Emprestar livro pra algum membro
4) Registrar devolução de livro
5) Remover membro
6) Remover livro
7) Pesquisar livro por título, autor ou ID
8) Listar todos os membros
9) Listar todos os livros
10) Listar livros disponíveis para empréstimo
11) Listar todos os livros emprestados
''')
    escolha = int(input('Digite o número correspondente ao que deseja fazer: '))
    print('-'*50)
    if escolha == 1:
        titulo = input('Digite o título do livro: ')
        autor = input('Digite o nome do autor do livro: ')
        livro = Livro(titulo, autor)
        biblioteca.adicionar_livros(livro)
        print('='*50)
        
    elif escolha == 2:
        nome = input('Digite o nome do membro: ')
        numero_de_membro = int(input('Digite o número do membro: '))
        membro = Membro(nome, numero_de_membro)
        biblioteca.adicionar_membro(membro)
        print('='*50)
        
    elif escolha == 3:
        titulo = input('Digite o título do livro: ')
        membro = input('Digite o nome do membro que você deseja emprestar esse livro: ')
        biblioteca.emprestar_livro(titulo, membro)
        print('='*50)
        
    elif escolha == 4:
        titulo = input('Digite o título do livro: ')
        biblioteca.registar_devolucao(titulo)
        print('='*50)
        
    elif escolha == 5:
        nome = input('Digite o nome do membro que deseja remover: ')
        biblioteca.remover_membro(nome)
        print('='*50)
        
    elif escolha == 6:
        titulo = input('Digite o título do livro: ')
        biblioteca.remover_livro(titulo)
        print('='*50)
        
    elif escolha == 7:
        biblioteca.pesquisar_livros()
        print('='*50)
        
    elif escolha == 8:
        biblioteca.listar_membros()
        print('='*50)
        
    elif escolha == 9:
        biblioteca.listar_livros()
        print('='*50)
        
    elif escolha == 10:
        biblioteca.listar_livros_disponiveis()
        print('='*50)
        
    elif escolha == 11:
        biblioteca.listar_livros_emprestados()
        print('='*50)
        
    continuacao = input('Você deseja continuar o programa? Digite Y para sim e N para não: ')
    print('='*50)
    
print('Obrigado por usar meu programa!')
a = input('Digite enter para sair... ')