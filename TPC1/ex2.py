#Exercício 2
def contagem(string):
    contador=0
    for letra in string:
        if letra=="A" or letra=="a":
            contador=contador + 1
    return contador

s="Sou a Helena e estou na cadeira de PLN."
print(contagem(s))