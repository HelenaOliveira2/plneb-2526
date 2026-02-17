#Exercício 7
def balanceadas(s1,s2):
    for letra in s1:
        if letra not in s2: 
            return False
    return True

print(balanceadas("Mestrado","Dia"))
print(balanceadas("casa","casal"))
