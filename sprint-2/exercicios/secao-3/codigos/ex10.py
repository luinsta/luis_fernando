def soma_numeros_em_string(s):
    numeros = s.split(',')
    numeros_int = [int(num) for num in numeros]
    return sum(numeros_int)

entrada = "1,3,4,6,10,76"
resultado = soma_numeros_em_string(entrada)
print(resultado)
