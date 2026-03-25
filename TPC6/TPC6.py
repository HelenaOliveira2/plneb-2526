import spacy
import json

nlp = spacy.load("pt_core_news_lg")

f =open("Harry Potter e A Pedra Filosofal.txt","r", encoding="utf-8")
texto = f.read()
f.close()

# Substitui as quebras de linha e as quebras de página
texto = texto.replace('\n', ' ').replace('\f', ' ')

doc = nlp(texto)

amigos = {}

for sent in doc.sents:
    personagens_frase = []
    
    for entity in sent.ents:
        if entity.label_ == "PER":
            nome = entity.text.strip()
            if nome not in personagens_frase and len(nome) > 1:
                personagens_frase.append(nome)
                
    if len(personagens_frase) > 1:
        for p1 in personagens_frase:
            if p1 not in amigos:
                amigos[p1] = {}
                
            for p2 in personagens_frase:
                if p1 != p2:
                    if p2 not in amigos[p1]:
                        amigos[p1][p2] = 1
                    else:
                        amigos[p1][p2] += 1

amigos_ordenados = {}
for personagem, relacoes in amigos.items():
    relacoes_ordenadas = sorted(relacoes.items(), key=lambda x: x[1], reverse=True)
    amigos_ordenados[personagem] = dict(relacoes_ordenadas)

f_out = open("HarryFriends.json", "w", encoding="utf8")
json.dump(amigos_ordenados, f_out, indent=4, ensure_ascii=False)
f_out.close()