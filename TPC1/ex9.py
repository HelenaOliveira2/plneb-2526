#Exercício 9
def anagrama(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    return sorted(s1) == sorted(s2)
    
print(anagrama("listen","silent"))
print(anagrama("hello","world"))
