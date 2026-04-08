def ocorrencias_freq(nome):
    f = open(nome)
    ficheiro = f.read()
    lista_palavras=ficheiro.split()
    contagem = {}
    for palavra in lista_palavras:
        if palavra in contagem:
            contagem[palavra] = contagem[palavra] + 1
        else:
            contagem[palavra] = 1
    lista = []
    



    