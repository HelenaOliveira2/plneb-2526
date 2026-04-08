import spacy

#nlp = spacy.load("pt_core_news_sm")
nlp = spacy.load("pt_core_news_lg")

texto = "Luís Montenegro respondia à líder da Iniciativa Liberal, Mariana Leitão, que pouco antes considerara que a proposta de lei laboral estava destinada ao fracasso, classificando também como obsoleto o atual modelo de concertação. O governo quer fazer uma reforma laboral do século XXI com uma concertação social do século XIX, afirmou Leitão, recordando que os sindicatos representam somente sete por cento dos trabalhadores portugueses."

doc = nlp(texto)

print("="*20, "Entities", "="*20)

for entity in doc.ents:
    if entity.label_ == "PER" or entity.label_ == "ORG":
        print(entity, entity.label_)