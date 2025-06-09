from crear_cartas import Carta 
from crear_baraja import Baraja

def main():
    baraja = Baraja()
    baraja.barajar()
    print(f"Cartas repartidas: {baraja.repartir(5)}")

if __name__ == "__main__": main()