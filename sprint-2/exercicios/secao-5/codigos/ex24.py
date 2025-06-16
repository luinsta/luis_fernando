import csv
def formatar_media(media):
    return f'{media:.1f}' if media * 10 % 1 == 0 else f'{media:.2f}'

with open('estudantes.csv', encoding='utf-8') as arq:
    alunos = [
        (
            linha[0],
            sorted(
                list(map(lambda n: float(n), linha[1:])),
                reverse=True
            )[:3]
        )
        for linha in csv.reader(arq)
    ]

for nome, notas in sorted(alunos, key=lambda x: x[0]):
    media = round(sum(notas) / 3, 2)
    print(f'Nome: {nome} Notas: {list(map(int, notas))} Média: {formatar_media(media)}')
