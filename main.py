from src.cartas.crear_cartas import Carta 
from src.cartas.crear_baraja import Baraja
from src.cartas.evaluar_mano import Analizar

def main():
    baraja = Baraja(num_barajas=2)
    baraja.barajar()
    mano = baraja.repartir(5)
    resultado = Analizar(mano).mejor_mano
    print(f"Resultado: {resultado}")
    
if __name__ == "__main__": main()