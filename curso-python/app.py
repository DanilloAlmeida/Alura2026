from modelos.restaurante import Restaurante

restaurante1 = Restaurante("La Buena Mesa", "Mexicana")
restaurante2 = Restaurante("El Sabor", "Italiana")
restaurante3 = Restaurante("Sabor do Brasil", "Brasileira")

restaurante1.receber_avaliacao("João", 5)
restaurante1.receber_avaliacao("Gui", 10)
restaurante1.receber_avaliacao("Lais", 7)


restaurante3.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()