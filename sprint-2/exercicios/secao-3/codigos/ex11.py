def dividir_em_tres(lista):
    tamanho = len(lista) // 3
    parte1 = lista[:tamanho]
    parte2 = lista[tamanho:2*tamanho]
    parte3 = lista[2*tamanho:]
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
p1, p2, p3 = dividir_em_tres(lista)

print(f"{p1} {p2} {p3}")