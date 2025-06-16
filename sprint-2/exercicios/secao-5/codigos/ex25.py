def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)
    filtrados = filter(lambda item: item[1] > media, conteudo.items())
    return sorted(filtrados, key=lambda x: x[1])
