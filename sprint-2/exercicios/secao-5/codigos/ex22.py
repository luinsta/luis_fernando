from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    return reduce(lambda acc, val: acc + val, valores)
