#Exercício 3
def vogais(string):
    contador=0
    s=string.upper()
    for letra in s:
        if letra in ["A","E","I","O","U"]:
            contador=contador + 1
    return contador

s="Sou a Helena e estou na cadeira de PLN."
print(vogais(s))