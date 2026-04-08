import re

text='Está tudo bem Tom? EEEEEEEEEEEE Tudo perfeitoooooo neste ano de 2026, 3,1416. Maravilhoso, muito Mesmo!!!!!!'
# 1. have a 't'
print(re.findall(r't',text))

# 2. have a 't' or a 'T'
print(re.findall(r'[Tt]',text))

# 3. have a letter (and how many)
letras = re.findall(r'[a-zA-Z]', text)
print(letras)
print("Total de letras:", len(letras))

# 4. have a digit
print(re.findall(r'\d',text))

# 5. have a decimal number
print(re.findall(r'\d+,\d+',text))

# 6. have a length higher than 3 characters
print(re.findall(r'\b\w{4,}\b',text))

# 7. have an 'M' but not an 'm'
print(re.findall(r'\b[^m\s]*M[^m\s]*\b', text))

# 8. have a character repeated twice
print(re.findall(r'\b\w*(\w)\w*\1\w*\b',text))

# 9. Have only one character repeated many times
print(re.findall(r'\b(\w)\1+\b', text)) # se for uma letra sozinha sem estar em palavra
print(re.findall(r'(.)\1{2,}', text)) # se for uma letra numa palavra 

# 10. put all words between {}
print(re.sub(r'(\w+)', r'{\1}', text)) # re.sub(o_que_procurar, pelo_que_substituir, texto_original)