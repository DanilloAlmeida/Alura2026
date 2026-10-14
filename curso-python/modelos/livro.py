class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} - por - {self.autor} ({self.paginas} páginas)'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'


    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

Livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', 1178)
Livro2 = Livro('O Hobbit', 'J.R.R. Tolkien', 310)

print(Livro1)
print(Livro2)
print(Livro1.titulo_autor)
print(Livro2.titulo_autor)