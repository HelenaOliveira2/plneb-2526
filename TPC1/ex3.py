#Exercício 3
def vogais(string):
    contador=0
    s=string.upper()
    for caracter in s:
        if caracter in "AEIOU":
            contador=contador + 1
    return contador

s="Mestrado"
print(vogais(s))