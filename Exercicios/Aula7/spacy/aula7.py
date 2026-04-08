import spacy

nlp = spacy.load("./models/models-best")

f = open("C:\\Users\\helen\\Desktop\\Mestrado\\2Semestre\\PLN\\plneb-2526-stor\\Dados\\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf8")
texto = f.read()


# .\aula7 > text.txt

config={
    "overwrite_ents": True
}

ruler = nlp.add_pipe("entity_ruler", last=True, config=config) #before, after, first

patterns = [
    {"label": "Pessoa", "pattern": "Dumbledore"}, 
    {"label": "Pessoa", "pattern": "Hagrid"}, 
    {"label": "Pessoa", "pattern": [{"LOWER": "albus"}, {"LOWER": "dumbledore"}]}, 
]

ruler.add_patterns(patterns)

doc = nlp(texto)

for ent in doc.ents:
    print(ent, ent.label_)