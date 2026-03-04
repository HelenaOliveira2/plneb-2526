import re

# ler ficheiro txt
f = open("dicionario_medico.txt","r", encoding="utf8") #enconding="utf8"
texto = f.read()


# ----------------- TRATAR QUEBRAS DE PÁGINA -----------------
# Caso 1: quebra de página entre termo e definição
texto = re.sub(r"\n\n([^\n]+)\n\n\f", r"\n\n\1\n", texto)

# Caso 2: quebra de página dentro de definição longa
texto = re.sub(r"\n\n\f([\s\S]*?)\n\n", r" \1\n\n", texto)

# Caso 3: \f soltos
texto = re.sub(r"\f", "", texto)

# ----------------- JUNTAR LINHAS QUEBRADAS DENTRO DE DESCRIÇÃO -----------------
# Se a linha começa com minúscula ou acento, junta com a anterior
texto = re.sub(r'\n([a-zà-ú])', r' \1', texto)

# ----------------- REMOVER LINHAS VAZIAS EXTRAS -----------------
texto = re.sub(r'\n\s*\n', '\n\n', texto)

# ----------------- MARCAR TERMOS -----------------
# Marca com @ o início do termo, assumindo que ele começa com letra maiúscula
texto = re.sub(r'\n([A-ZÀ-Ú][^\n]*)', r'\n\n@\1', texto)

# ----------------- DIVIDIR CONCEITOS -----------------
conceitos = re.split(r'\n\n@', texto)

print(conceitos)
print(len(conceitos))

def limpa_descricao(descricao):
    descricao = re.sub(r'\n',' ',descricao)
    descricao= descricao.strip() # tira os espaços que estão antes e depois da descricao
    return descricao

conceitos_dict={}

for c in conceitos[1:]:
    elems=re.split(r'\n',c, maxsplit=1)
    if len(elems)>1:
        descricao=elems[0]
        designacao=elems[1]
        #print('designação:' , designacao)
 
        #print('descrição:' , descricao)
        #print("-"*20)
        conceitos_dict[designacao]=limpa_descricao(descricao)
    else:
        #Fixe me
        continue
        
print (conceitos_dict)
print(len(conceitos_dict))



#------------------------------------------------------------------------------------
import json 

def gera_json(filename, conceitos_dict):
    f_out = open(filename,'w', encoding='utf8')
    json.dump(conceitos_dict,f_out, indent=4, ensure_ascii=False) # o ident é para nao ficar tudo numa linha, e o ensure é para os acentos ficarem direito

#gera_json
gera_json('dicionario_medico.json', conceitos_dict)

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


#json.load() #ler o ficheiro
#json.dump() #escrever no ficheiro

#for c in conceitos[1:]:
    #print (c)
    #break
