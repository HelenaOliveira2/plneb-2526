#Exercício 8
def conta_ocorrencias(s1, s2):
    contador = 0
    tamanho = len(s1)
    for i in range(len(s2) - tamanho + 1):
        if s2[i : i + tamanho] == s1:
            contador = contador + 1
    return contador

print(conta_ocorrencias("helena","helenaaahelena"))

# ou, utilizando a função count:
def conta_ocorrencias1(s1, s2):
    return s2.count(s1)