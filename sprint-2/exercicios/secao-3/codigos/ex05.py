import json

with open('person.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)