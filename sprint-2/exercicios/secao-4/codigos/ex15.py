class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        print("Emitindo som...")

class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

# Testando as classes
print("Pato")
pato = Pato()
pato.voar()
pato.emitir_som()

print("Pardal")
pardal = Pardal()
pardal.voar()
pardal.emitir_som()
