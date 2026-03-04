import re

# ler ficheiro txt
f = open("dicionario_medico.txt","r", encoding="utf8") #enconding="utf8"
texto = f.read()


#------------------ RETIRAR ESPAÇOS DE MUDANÇA DE PÁGINA ------------------

#--- Caso 1: quebra de página entre termo e definição ---
# Ex.: "\n\nTermo\n\n\f" vira "\n\nTermo\n"
texto = re.sub(r"\n\n([^\n]+)\n\n\f", r"\n\n\1\n", texto)

#--- Caso 2: quebra de página dentro de uma definição longa ---
# Este captura qualquer conteúdo entre "\n\n\f" e "\n\n" sem quebrar linhas internas
# Forma segura mesmo quando a definição tem múltiplas linhas
texto = re.sub(r"\n\n\f([\s\S]*?)\n\n", r" \1\n\n", texto)

#--- Caso 3: quebra de página no início de um termo (ex.: "\fTermo") ---
# Remove qualquer \f solto
texto = re.sub(r"\f", "", texto)


#------------------ CAPTURAR OS CONCEITOS ------------------
# Agora cada conceito está separado por dupla quebra de linha
conceitos = re.split(r"\n\n", texto)

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
        designacao=elems[0]
        #print('designação:' , designacao)
        descricao=elems[1]
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
