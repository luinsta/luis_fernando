with open('number.txt', 'r') as f:
    numeros = list(map(int, f))

pares = list(filter(lambda x: x % 2 == 0, numeros))

maiores_pares = sorted(pares, reverse=True)[:5]

print(f"{maiores_pares}")
print(f"{sum(maiores_pares)}")