#Exercício 6
def capicua(string):
    s = string.lower()
    return s==s[::-1]

print(capicua("Ana"))
print(capicua("Helena"))