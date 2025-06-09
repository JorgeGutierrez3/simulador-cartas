class Carta(): 
    
    PICAS =['corazon', 'diamante', 'trebol', 'pica']
    NUMEROS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self,numero, pica): 
        self.numero = numero
        self.pica = pica
    
    def __str__(self): return f"{self.numero} de {self.pica}"