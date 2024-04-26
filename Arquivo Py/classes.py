class Livro:
    contagem = 0
    
    def __init__(self, titulo, autor):
        Livro.contagem += 1
        self.titulo = titulo
        self.autor = autor
        self.id = Livro.contagem
        self.estado_de_emprestimo = 'disponível'


class Membro:
    def __init__(self, nome, numero_de_membro):
        self.nome = nome
        self.numero_de_membro = numero_de_membro
        self.historico_de_livros_emprestados = []


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros_disponiveis = []
        self.livros_emprestados = {}
        self.lista_de_membros = []
        self.lista_de_autores = []
        self.lista_de_ids = []
        self.livros_totais = []

    def adicionar_livros(self, livro):
        self.livros_totais.append(livro)
        self.livros_disponiveis.append(livro)
        self.lista_de_autores.append(livro.autor)
        self.lista_de_ids.append(livro.id)
        print(f'Livro {livro.titulo} adicionado!')

    def adicionar_membro(self, membro):
        self.lista_de_membros.append(membro)
        print(f'Membro {membro.nome} adicionado!')

    def emprestar_livro(self, titulo, nome_membro):
        livro_encontrado = None
        for livro in self.livros_disponiveis:
            if livro.titulo.lower() == titulo.lower():
                livro_encontrado = livro
                break
        
        membro_encontrado = None
        for membro in self.lista_de_membros:
            if membro.nome.lower() == nome_membro.lower():
                membro_encontrado = membro
                break
        
        if livro_encontrado and membro_encontrado:
            self.livros_disponiveis.remove(livro_encontrado)
            self.livros_emprestados[livro_encontrado] = membro_encontrado
            livro_encontrado.estado_de_emprestimo = 'emprestado'
            membro_encontrado.historico_de_livros_emprestados.append(f'{livro_encontrado.titulo}!')
            print(f'O livro "{livro_encontrado.titulo}" foi emprestado para o membro "{membro_encontrado.nome}"!')
        else:
            print('Não foi possível realizar o empréstimo.')

    def registar_devolucao(self, titulo):
        livro_encontrado = None
        for livro, membro in self.livros_emprestados.items():
            if livro.titulo.lower() == titulo.lower():
                livro_encontrado = livro
                break
        
        if livro_encontrado:
            self.livros_disponiveis.append(livro_encontrado)
            self.livros_emprestados.pop(livro_encontrado)
            livro_encontrado.estado_de_emprestimo = 'disponível'
            print(f'O livro "{livro_encontrado.titulo}" foi devolvido com sucesso!')
        else:
            print('Não foi possível registrar a devolução. Verifique se o livro está emprestado e se o título está correto.')
            
    def pesquisar_livros(self):
        print('''
De que forma deseja pesquisar?

1) Por título do livro
2) Por autor do livro
3) Por ID do livro
''')
        escolha_pesquisa = int(input('Digite o número corresponde a sua escolha: '))
        print('-'*50)
        
        if escolha_pesquisa == 1:
            livro_desejado = input('Digite o título do livro desejado: ')
            for livro in self.livros_totais:
                if livro.titulo.lower() == livro_desejado.lower():
                    print(f'''
Livro encontrado:
Título: {livro.titulo}
Autor: {livro.autor}
ID: {livro.id}
Status: {livro.estado_de_emprestimo}
''')
                    return
            print('Livro não encontrado!')
        
        elif escolha_pesquisa == 2:
            autor_desejado = input('Digite o autor desejado: ')
            for livro in self.livros_totais:
                if livro.autor.lower() == autor_desejado.lower():
                    print(f'''
Livro encontrado:
Título: {livro.titulo}
Autor: {livro.autor}
ID: {livro.id}
Status: {livro.estado_de_emprestimo}
''')
                    return
            print('Autor não encontrado!')
        
        elif escolha_pesquisa == 3:
            id_desejado = int(input('Digite o ID desejado: '))
            for livro in self.livros_totais:
                if livro.id == id_desejado:
                    print(f'''
Livro encontrado:
Título: {livro.titulo}
Autor: {livro.autor}
ID: {livro.id}
Status: {livro.estado_de_emprestimo}
''')
                    return
            print('ID não encontrado!')

    def remover_livro(self, titulo):
        livro_encontrado = None
        for livro in self.livros_totais:
            if livro.titulo.lower() == titulo.lower():
                livro_encontrado = livro
                break
        
        if livro_encontrado:
            if livro_encontrado in self.livros_emprestados:
                print('O livro está com um membro, não pode ser removido sem estar disponível!')

            elif livro_encontrado in self.livros_disponiveis:
                self.lista_de_autores.remove(livro_encontrado.autor)
                self.livros_totais.remove(livro_encontrado)
                self.lista_de_ids.remove(livro_encontrado.id)
                self.livros_disponiveis.remove(livro_encontrado)
                print(f'O livro "{livro_encontrado.titulo}" foi removido com sucesso!')
            
        else:
            print('Não foi possível encontrar um livro com esse título na biblioteca.')

    def remover_membro(self, nome):
        membro_encontrado = None
        for membro in self.lista_de_membros:
            if membro.nome.lower() == nome.lower():
                membro_encontrado = membro
                break
        
        if membro_encontrado:
            self.lista_de_membros.remove(membro_encontrado)
            print(f'O membro "{membro_encontrado.nome}" foi removido com sucesso!')
        else:
            print('Não foi possível encontrar um membro com esse nome na biblioteca.')

    def listar_livros(self):
        if len(self.livros_totais) > 0:
            print('Aqui vai uma lista de livros: ')
            print('-'*50)
            for livro in self.livros_totais:
                print(f'''
Livro encontrado:
Título: {livro.titulo}
Autor: {livro.autor}
ID: {livro.id}
Status: {livro.estado_de_emprestimo}
''')
                print('-'*50)
        else:
            print('Não há livros nessa biblioteca!')

    def listar_membros(self):
        if len(self.lista_de_membros) > 0:
            print('Aqui vai uma lista de membros: ')
            print('-'*50)
            for membro in self.lista_de_membros:
                print(f'''
Membro encontrado:
Nome: {membro.nome}
Número de membro: {membro.numero_de_membro}
Histórico de livros emprestados: {membro.historico_de_livros_emprestados}
''')
                print('-'*50)
        else:
            print('Não há membros que participam dessa biblioteca!')

    def listar_livros_disponiveis(self):
        if len(self.livros_disponiveis) > 0:
            print('Aqui vai uma lista de livros disponíveis: ')
            print('-'*50)
            for livro in self.livros_disponiveis:
                print(f'''
Livro encontrado:
Título: {livro.titulo}
Autor: {livro.autor}
ID: {livro.id}
''')
                print('-'*50)
        else:
            print('Não há livros disponíveis nessa biblioteca!')

    def listar_livros_emprestados(self):
        if len(self.livros_emprestados) > 0:
            print('Aqui vai uma lista de livros emprestados: ')
            print('-'*50)
            for livro, membro in self.livros_emprestados.items():
                print(f'''
Livro encontrado:
Título: {livro.titulo}
Autor: {livro.autor}
ID: {livro.id}
Status: {livro.estado_de_emprestimo}
Membro que está com ele: {membro.nome}
''')
                print('-'*50)
        else:
            print('Não há livros emprestados nessa biblioteca!')
