def my_map(lista, f):
    nova_lista = []
    for item in lista:
        nova_lista.append(f(item))
    return nova_lista
    
    
def carioca(x):
    x = x ** 2
    return x

entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(entrada, carioca)

print(resultado)