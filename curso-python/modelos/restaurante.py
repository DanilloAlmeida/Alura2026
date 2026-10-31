from modelos.avaliacao import Avaliacao


class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        # self._capacidade = capacidade       

        Restaurante.restaurantes.append(self)

    
    def __str__(self):
        return f'{self._nome} - {self._categoria}'

    @classmethod    
    def listar_restaurantes(cls):
        print(
            f"{'NOME DO RESTAURANTE'.ljust(25)} | "
            f"{'CATEGORIA'.ljust(15)} | "
            f"{'ATIVO'.ljust(5)} | "
            f"{'AVALIAÇÃO'.ljust(9)} |"
        )
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | "
                f"{restaurante._categoria.ljust(15)} | "
                f"{restaurante.ativo.ljust(5)} | "
                f"{str(restaurante.media_avaliacoes).ljust(9)} |"
            )
            # print(f'{restaurante.capacidade} {''.ljust(24)} | {restaurante.nota_avaliacao}')

    @property    
    def ativo(self):
        return 'sim' if self._ativo else 'não'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(soma_das_notas / len(self._avaliacao), 1)

