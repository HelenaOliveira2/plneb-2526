#Exercício 2
def contagem(string):
    contador=0
    for caracter in string:
        if caracter=="A" or caracter=="a":
            contador=contador + 1
    return contador

s="Sou a Helena e estou na cadeira de PLN."
print(contagem(s))

# ou, utilizando a função count:
def contagem1(string):
    return string.count("a") + string.count("A")

