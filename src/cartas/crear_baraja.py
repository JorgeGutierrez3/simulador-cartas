from .crear_cartas import Carta
import random

class Baraja():
    def __init__(self):
        self.cartas = []
        for pica in Carta.PICAS:
            for numero in Carta.NUMEROS:
                self.cartas.append(Carta(numero, pica))

    def __str__(self):
        return ', '.join(str(carta) for carta in self.cartas)

    def barajar(self):
        random.shuffle(self.cartas)

    def repartir(self, num_cartas):
        if num_cartas > len(self.cartas):
            raise ValueError("No hay suficientes cartas en la baraja.")
        repartidas = self.cartas[:num_cartas]
        self.cartas = self.cartas[num_cartas:]
        return ', '.join(str(carta) for carta in repartidas)