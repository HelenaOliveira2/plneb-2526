from bs4 import BeautifulSoup
import requests
import json
import string

url = "https://www.atlasdasaude.pt/doencasaaz/"

def extrair_pagina(url):
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    div_doencas = soup.find_all("div", class_="views-row")
    #print (div_doencas)

    res={}
    for div in div_doencas:
        designacao=div.div.h3.a.text
        descricao=div.find("div", class_="views-field-body").div.text
        res[designacao]=descricao.strip()
    return res

res={}
for letra in string.ascii_lowercase:
    res = res | extrair_pagina(url+letra)

f_out=open("doencas.json","w", encoding="utf-8")
json.dump(res,f_out, indent=4, ensure_ascii=False)
f_out.close()



#selenium - comunicacao entre maquina e browser (curiosidade)
#pip install selenium