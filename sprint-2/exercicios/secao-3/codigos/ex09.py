class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada  # True se ligada, False se desligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada


lamp = Lampada(False)
lamp.liga()
print("A lâmpada está ligada?", lamp.esta_ligada()) 

lamp.desliga()
print("A lâmpada ainda está ligada?", lamp.esta_ligada()) 