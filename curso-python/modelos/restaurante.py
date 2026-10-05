class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, 
                 capacidade=0, nota_avaliacao=0.0,):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self.nota_avaliacao = nota_avaliacao
        self.capacidade = capacidade       

        Restaurante.restaurantes.append(self)

    
    def __str__(self):
        return f'{self.nome} - {self.categoria}'

    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} \t | Ativo: {restaurante.ativo.ljust(3)}')
            # print(f'{restaurante.capacidade} {''.ljust(24)} | {restaurante.nota_avaliacao}')
            
    @property    
    def ativo(self):
        return 'sim' if self._ativo else 'não'

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Italiana')
restaurante_exemplo = Restaurante(
    nome='Comida Boa',
    categoria='Gourmet',
    # capacidade=50,
    # nota_avaliacao=4.5,
    # ativo=True
)

Restaurante.listar_restaurantes()