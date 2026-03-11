import re
import json

#pdftotext -l 50 LIVRO-Doenças-do-Aparelho-Digestivo.pdf --> livrinho

# ler ficheiro txt
f = open("livrinho.txt","r", encoding="utf8") #enconding="utf8"
texto = f.read()

f_conceitos=open("conceitos.json", encoding="utf-8")
conceitos=json.load(f_conceitos)  #load() - json; read() - text

black_list=["de","e","os"]

def substituir_conceito(match):
    palavra=match[0]
    if palavra in conceitos and palavra not in black_list:
        return f"<a href='' title='{conceitos[palavra]}'>{palavra}</a>"
    else:
        return palavra


#### encontrar/substituir conceitos
texto=re.sub(r'\w+',substituir_conceito,texto)
print(texto)

### gerar html
texto=re.sub(r'\n','<br>',texto)
texto=re.sub(r'\f', '<hr>', texto)

f_html=open("livro.html","w", encoding="utf-8")

html_header="""
<html>
    <head>
        <title> Livro de doenças do aparelho digestivo </title>
        <meta charset="utf-8">
    </head>
"""

html_body = f'<body> {texto} </body>'

html_footer = '</html>'

f_html=open("livro.html","w", encoding="utf-8")
f_html.write(html_header + html_body + html_footer)
