class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, 
                 capacidade=0, nota_avaliacao=0.0,):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self.nota_avaliacao = nota_avaliacao
        self.capacidade = capacidade       

        Restaurante.restaurantes.append(self)

    
    def __str__(self):
        return f'{self._nome} - {self._categoria}'

    @classmethod    
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} \t | Ativo: {restaurante.ativo.ljust(3)}')
            # print(f'{restaurante.capacidade} {''.ljust(24)} | {restaurante.nota_avaliacao}')
            
    @property
    def nome(self):
        self._ativo = not self._ativo

    @property    
    def ativo(self):
        return 'sim' if self._ativo else 'não'

# restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_pizza = Restaurante('pizza', 'Italiana')
# # restaurante_pizza.nome = 'Pizza Bella'
# restaurante_pizza._nome = 'Pizza Bella'
# restaurante_burger = Restaurante('burger', 'Fast Food')
# restaurante_burger._nome = 'Burger King' 
# restaurante_burger._ativo = True

# restaurante_exemplo = Restaurante(
#     nome='COMIDA BOA',
#     categoria='Gourmet',
#     # capacidade=50,
#     # nota_avaliacao=4.5,
#     # ativo=True
# )

# Restaurante.listar_restaurantes()