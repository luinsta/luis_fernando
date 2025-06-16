with open('arquivo_texto.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha, end='')  