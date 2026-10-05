class Carro:

    carros = []

    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano  
        self.cor = cor

        Carro.carros.append(self)

    def __str__(self):
        return f'{self.modelo} - {self.ano} - {self.cor}'

    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo} \t | {carro.ano} \t | {carro.cor}')

carro_exemplo1 = Carro('Fusca', 1980, 'Azul')
carro_exemplo2 = Carro('Fusca2', 1990, 'Azul')
carro_exemplo3 = Carro('Fusca3', 1950, 'Azul')
carro_exemplo4 = Carro('Fusca4', 1970, 'Azul')

# print(carro_exemplo)
Carro.listar_carros()