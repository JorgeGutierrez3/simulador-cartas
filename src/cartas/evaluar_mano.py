from collections import Counter
from .crear_cartas import Carta
class Analizar():
    def __init__(self, cartas):
        self.cartas = cartas
        self.mejor_mano = self.evaluar_manos()
            
    def evaluar_manos(self):
        cuenta = Counter([(carta.numero) for carta in self.cartas])      
        frequencias = dict(sorted(cuenta.items(), key=lambda item: item[1], reverse=True))
        orden = sorted([(carta.valor) for carta in self.cartas], reverse=True)
        self.cartas.sort(key=lambda carta: carta.valor, reverse=True)
        print(', '.join(str(carta) for carta in self.cartas))
        #print(f"Frecuencias de cartas: {(cuenta)}") 

        if list(frequencias.values()) == [4, 1]:
            self.mejor_mano = "Póker de " + list(frequencias.keys())[0]
        elif list(frequencias.values()) == [3, 2]:
            self.mejor_mano = "Full House de " + ' y '.join(list(frequencias.keys()))
        elif list(frequencias.values()) == [3, 1, 1]:
            self.mejor_mano = f"Trío de {list(frequencias.keys())[0]}"
        elif list(frequencias.values()) == [2, 2, 1]:
            self.mejor_mano = "Doble Pareja de " + ' y '.join(list(frequencias.keys())[0:2])
        elif list(frequencias.values()) == [2, 1, 1, 1]:
            self.mejor_mano = f"Pareja de {list(frequencias.keys())[0]}"
        elif len(set(carta.palo for carta in self.cartas)) == 1:
            self.mejor_mano = "Color"
        elif (max(orden) - min(orden) == 4) or orden == [14, 5, 4, 3, 2]:  # Considera el As como 1 en la escalera
                self.mejor_mano = "Escalera"
                if len(set(carta.palo for carta in self.cartas)) == 1:
                    self.mejor_mano = "Escalera de Color"
                elif set(orden) == {14, 13, 12, 11, 10}:
                    self.mejor_mano = "Escalera Real"
        else:
            self.mejor_mano = "Carta Alta"
        return self.mejor_mano
            

