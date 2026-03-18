from bs4 import BeautifulSoup
import requests
import json
import string

base_url = "https://www.atlasdasaude.pt"
url = base_url + "/doencasaaz/"

def extrair_fulldesc(link):
    html = requests.get(link).text
    soup = BeautifulSoup(html, "html.parser")

    conteudo = soup.find("div", class_="field field-name-body field-type-text-with-summary field-label-hidden")
          
    return conteudo.text.strip() 


def extrair_pagina(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    div_doencas = soup.find_all("div", class_="views-row")

    res={}
    for div in div_doencas:
        designacao=div.div.h3.a.text
        descricao=div.find("div", class_="views-field-body").div.text

        link = base_url + div.div.h3.a["href"] 

        fulldesc = extrair_fulldesc(link)

        res[designacao] = {
            "shortdesc": descricao.strip(),
            "fulldesc": fulldesc
        }

    return res


res={}
for letra in string.ascii_lowercase:
    res = res | extrair_pagina(url+letra)

f_out=open("doencas_tudo.json","w", encoding="utf-8")
json.dump(res,f_out, indent=4, ensure_ascii=False)
f_out.close()
