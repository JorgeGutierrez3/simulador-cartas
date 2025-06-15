class Carta(): 
    
    PALOS =['corazon', 'diamante', 'trebol', 'palo']
    NUMEROS = {
        '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9,
        '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def __init__(self, numero, palo, valor):
        self.numero = numero
        self.palo = palo
        self.valor = valor
        
    def __str__(self): return f"{self.numero} de {self.palo}"