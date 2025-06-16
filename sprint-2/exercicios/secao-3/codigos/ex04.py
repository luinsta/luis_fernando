def remover_duplicatas(lista):
    return list(set(lista))


lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
resultado = remover_duplicatas(lista_teste)
print(resultado)