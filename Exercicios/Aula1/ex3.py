def ficheiro_inverso(nome):
    f = open(nome)
    ficheiro = f.read()
    linhas=ficheiro.split("\n")
    print(linhas[::-1])

ficheiro_inverso("C:\\Users\\helen\\Desktop\\Mestrado\\2º Semestre\\PLN\\plneb-2526\\Exercícios\\Aula1\\ex1.py")

