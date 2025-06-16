def calcular_valor_maximo(operadores, operandos) -> float:
    resultados = map(lambda x: eval(f"{x[1][0]}{x[0]}{x[1][1]}"), zip(operadores, operandos))
    return max(resultados)
