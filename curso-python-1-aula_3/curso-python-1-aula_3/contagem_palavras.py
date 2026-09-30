credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
contagem_palavras['elemento1'] = 10
contagem_palavras['elemento2'] = 20
contagem_palavras['nova_chave'] = 'resolvi colocar texto'
print (contagem_palavras)
palavras = frase.split()
print (palavras)
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)