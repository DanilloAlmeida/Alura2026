class Livro:

    livros = []


    def __init__(self, titulo='', autor='', ano_publicacao=0):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        self.livros.append(self)

    def __str__(self):
        return f'{self.titulo} - por - {self.autor} ({self.ano_publicacao}) \t {"Disponível" if self.disponivel else "Indisponível"}'

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False

    @staticmethod
    def verificar_disponibilidade(ano_publicacao):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano_publicacao:
                livros_disponiveis.append(livro)
        if livros_disponiveis == []:
            print(f'Não há livros disponíveis do ano {ano_publicacao}.')        
        return livros_disponiveis

livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkin', 1954)
livro2 = Livro('O Hobbit', 'J.R.R. Tolkin', 1954)
livro3 = Livro('O Hobbit3', 'J.R.R. Tolkin', 1954)
livro4 = Livro('O Hobbit4', 'J.R.R. Tolkin', 1954)
print(livro1)
print(livro2)
print(livro3)
print(livro4)
print('### executando emprestimo livro1 ###')
livro1.emprestar()
print(livro1)
print('### executando verificação de disponibilidade ###')
print (Livro.verificar_disponibilidade(1954))