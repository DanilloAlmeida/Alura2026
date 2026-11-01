from livro2 import Livro

livroAA = Livro('O Senhor dos AA', 'J.A.A.', 1954)
livroAA.emprestar()
# print(livroAA)

print('\n\n ###    executando arquivo biblioteca.py    ###\n\n')
print('\n\n ###    executando verificação de disponibilidade    ###')

livros = Livro.verificar_disponibilidade(1954)

if livros:
    for livro in livros:
        print(livro)
else:
    print('Não há livros disponíveis desse ano.')