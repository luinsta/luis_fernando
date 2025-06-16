class Ordenadora:
    def __init__(self, lista):
        self.listaBaguncada = lista

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

print(crescente.ordenacaoCrescente())   # [1, 2, 3, 4, 5]
print(decrescente.ordenacaoDecrescente())  # [9, 8, 7, 6]
