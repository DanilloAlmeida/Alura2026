from modelos.restaurante import Restaurante

restaurante1 = Restaurante("La Buena Mesa", "Mexicana", 50, 4.5)
restaurante2 = Restaurante("El Sabor", "Italiana", 30, 4.0)
restaurante3 = Restaurante("Sabor do Brasil", "Brasileira", 40, 4.2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()