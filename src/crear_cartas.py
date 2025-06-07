class Carta(): 
    def __init__(self,numero, pica): 
        self.numero = numero 
        self.pica = pica 
    def __str__(self): return f"{self.numero} de {self.pica}"