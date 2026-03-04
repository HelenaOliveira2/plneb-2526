import re
import json

# --------- ler ficheiro txt ------------
f = open("dicionario_medico.txt","r", encoding="utf8") #enconding="utf8"
texto = f.read()

# Marcar cada conceito com '@' 
texto = re.sub(r'\n\n', '\n\n@', texto)

# Substituir quebras de página por nova linha
texto = re.sub(r'\f', '\n', texto)

# Corrigir quebras entre definição e conceito (linha começa com maiúscula)
texto = re.sub(r'\n\n@\n([A-ZÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜÇ])', r'\n\1', texto)

# Juntar linhas quebradas dentro da descrição (minúsculas no meio)
texto = re.sub(r'([a-zà-ú])\s*\n\n@\n\s*([a-zà-ú])', r'\1 \2', texto)

# Remover marcadores '@'
texto = re.sub(r'@', '', texto)

# Separar texto em lista de conceitos
conceitos = re.split(r"\n\n", texto)

print(conceitos)
print(len(conceitos))


# ----------- Limpar descrição --------------------
def limpa_descricao(descricao):
    descricao = re.sub(r'\n', ' ', descricao)
    descricao = descricao.strip()
    return descricao

#--------- Criar dicionário --------------
conceitos_dict={}

for c in conceitos[1:]:
    elems=re.split(r'\n',c, maxsplit=1)
    if len(elems)>1:
        designacao=elems[0]
        descricao=elems[1]
        conceitos_dict[designacao]=limpa_descricao(descricao)
    else:
        #Fixe me
        continue
        
print (conceitos_dict)
print(len(conceitos_dict))
    

# ---------------- gerar json --------------------
def gera_json(filename, dicionario):
    with open(filename, 'w', encoding='utf8') as f_out:
        json.dump(dicionario, f_out, indent=4, ensure_ascii=False)

gera_json('dicionario_medico.json', conceitos_dict)

# ---------------- geral html --------------------
def gera_html(filename, conceitos_dict):
    html="""
<html>
    <head>
        <title> Dicionário Médico </title>
    </head>
    <body> """

    for c in conceitos_dict:
        html = html + f"""
        <div>
        <p> <b>{c} </b> </p>  
        <p> {conceitos_dict[c]} </p>
        </div>
        <hr>
"""

    html = html + """</body>
</html> """

    f_out = open(filename,'w', encoding='utf8')
    f_out.write(html)

gera_html("dicionario_medico.html", conceitos_dict)
