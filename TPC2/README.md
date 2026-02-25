# TPC2
Este diretório contém a resolução dos exercícios do TPC2, baseados na Ficha de Expressões Regulares 1.

- ex1.1.py: Verifica se a palavra "hello" está logo no início da frase. Recorre-se à função `re.match()` porque esta serve exatamente para procurar padrões a partir do começo da string.

- ex1.2.py: Procura a palavra "hello" em qualquer parte do texto. Neste caso, a escolha recai sobre o `re.search()`, que percorre a string toda até encontrar a palavra pretendida.

- ex1.3.py: Encontra todas as vezes que "hello" aparece na frase, independentemente de estar em maiúsculas ou minúsculas. O `re.findall()` devolve uma lista com tudo o que encontrou, sendo aplicada a *flag* `re.IGNORECASE` para ignorar as maiúsculas.

- ex1.4.py: Substitui todas as ocorrências de "hello" por "*YEP*". É utilizada a função `re.sub()` acompanhada pela *flag* `re.IGNORECASE` para apanhar os maiúsculos e minúsculos.

- ex1.5.py: Recebe uma linha de texto e corta-a em vários pedaços, usando a vírgula como separador. O `re.split()` corta o texto e devolve uma lista com as partes separadas.


- ex2.py (`palavra_magica(frase)`): Verifica se uma frase acaba com "por favor" seguido de um sinal de pontuação (`.`, `!`, `?`). Para garantir que isto só acontece no fim, junta-se o `re.search()` com o símbolo `$` no final da expressão.

- ex3.py (`narcissismo(linha)`): Conta quantas vezes a palavra "eu" aparece na string. A função utiliza o `re.findall` juntamente com a *flag* `re.IGNORECASE`, calculando de seguida o tamanho dessa lista através do `len()`.

- ex4.py (`troca_de_curso(linha, novo_curso)`): Substitui a sigla "LEI" pelo nome do curso ("Biomédica") passado à função no argumento `novo_curso`. O `re.sub()` faz esta troca de palavras.

- ex5.py (`soma_string(linha)`): Recebe uma string composta por números separados por vírgulas e calcula a sua soma. Primeiro, o `re.split` separa os números para uma lista e, depois, um ciclo `for` converte cada elemento para inteiro (`int`), acumulando o valor da soma.

- ex6.py (`pronomes(linha)`): Extrai todos os pronomes da frase. A função aplica o `re.findall` com `\b` (limites de palavra) à volta dos pronomes para não apanhar letras perdidas no meio de outras palavras, e utiliza a *flag* `re.IGNORECASE` para ignorar as maiúsculas.

- ex7.py (`variavel_valida(linha)`): Verifica se a string é um nome de variável válido (começar por letra e só ter letras, números ou *underscores*). O `re.match`, juntamente com o `^` no início e o `$` no fim (`r'^[a-zA-Z]\w*$'`), garante que a palavra toda é avaliada do início ao fim, rejeitando caracteres inválidos. Retorna True se a variável cumprir com os requisitos e False caso contrário.

- ex8.py (`inteiros(linha)`): Extrai números inteiros, positivos ou negativos, presentes no texto. A expressão regular utilizada é o `re.findall(r'-?\d+', linha)`, que procura por um sinal de menos opcional seguido de um ou mais dígitos.

- ex9.py (`underscores(linha)`): Substitui os espaços de uma string por *underscores*. Com o recurso a `re.sub(r'\s+', '_', linha)`, o `\s+` apanha todos os espaços (mesmo que estejam vários seguidos) e troca-os por um único `_`.

- ex10.py (`codigos_postais(lista)`): Recebe uma lista de códigos postais e separa as duas metades no sítio do hífen. Um ciclo `for` percorre os códigos, aplica o `re.split(r'-', codigo)` em cada um, e a lista resultante é adicionada a uma nova lista final através do método `.append()`.