from cartas import Carta 
from cartas import Baraja

def main():
    baraja = Baraja()
    baraja.barajar()
    print(f"Cartas repartidas: {baraja.repartir(5)}")

if __name__ == "__main__": main()