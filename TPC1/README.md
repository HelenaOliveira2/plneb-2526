# TPC1
Este diretório contém a resolução dos exercícios propostos no TPC1.
Cada exercício está num ficheiro separado (`ex1.py`, `ex2.py`, etc.), o que facilita a execução, a análise e a validação individual de cada algoritmo.

- ex1.py (`reverse(s)`): Recebe uma string e devolve a mesma invertida, utilizando slicing (`[::-1]`) por ser a forma mais direta.

- ex2.py (`contagem(s)`): Conta as ocorrências de "a" e "A" numa string.
Foram implementadas duas versões: uma manual, que utiliza uma variável `contador` iniciada a 0 e incrementada sempre que o ciclo `for` encontra uma das letras pretendidas; e outra com o método `.count()`, que simplifica o código.

- ex3.py (`vogais(s)`): Percorre a string e conta o número total de vogais.
A string é convertida para maiúsculas e cada carácter é comparado com a string "AEIOU", que contém as vogais. O contador é incrementado sempre que encontra uma dessas letras, garantindo que não há distinção entre maiúsculas e minúsculas.

- ex4.py (`minusculas(s)`): Converte todos os caracteres da string para minúsculas utilizando o método `.lower()`.

- ex5.py (`maiusculas(s)`): Converte todos os caracteres da string para maiúsculas utilizando o método `.upper()`.

- ex6.py (`capicua(s)`): Verifica se uma string é uma capicua comparando a original com a sua inversa. Utiliza `.lower()` para ignorar maiúsculas/minúsculas e `[::-1]` para inverter a string. 

- ex7.py (`balanceadas(s1,s2)`): Verifica se todos os caracteres de `s1` estão presentes em `s2`.
A função percorre cada letra de `s1` e usa o operador `not in` para detetar se alguma está ausente. Só retorna `True` se todas as letras forem encontradas.

- ex8.py (`conta_ocorrencias(s1,s2)`): Conta quantas vezes a substring `s1` aparece em `s2`.
Percorre cada posição `i` de `s2` e compara `s2[i : i + len(s1)]` com `s1`. O slicing garante que a parte analisada tem o mesmo tamanho de `s1` e o contador aumenta quando há coincidência. A versão alternativa usa `.count()` para simplificar.

- ex9.py (`anagrama(s1,s2)`): Determina se duas palavras são anagramas. As strings são convertidas para minúsculas com `.lower()`. Em seguida, `sorted()` organiza as letras de cada palavra em ordem alfabética. Por fim compara as listas resultantes para verificar se são iguais.
