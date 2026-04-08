from flask import Flask, render_template, request, redirect, session
import json
import random

app = Flask(__name__)

f_db=open("C:\\Users\\helen\\Desktop\\Mestrado\\2Semestre\\PLN\\plneb-2526\\TPC7\\dicionario_medico.json", "r", encoding="utf-8")
db = json.load(f_db)

@app.get("/")
def home_page():
    #  6 conceitos aleatórios
    primeiros_conceitos = random.sample(list(db.keys()), 6)
    return render_template("home.html", conceitos=primeiros_conceitos)

@app.get("/api/conceitos")
def conceitos_api():
    return db

@app.get("/conceitos")
def listar_conceitos():
    query = request.args.get("q", "").strip()
    if query:
        query_lower = query.lower()
        # Percorre o dicionário e compara tudo em minúsculas
        for chave in db.keys():
            if chave.lower() == query_lower:
                # Se encontrar, mostra a página do conceito com o nome original
                return render_template("conceito.html", designacao=chave, descricao=db[chave])
        
        # Se o ciclo terminar e não encontrar nada:
        return render_template("error.html", erro=f"O conceito '{query}' não existe no dicionário.")
    else:
        # Sem pesquisa, mostra o alfabeto
        return render_template("conceitos.html", conceitos=db.keys())


@app.get("/conceitos/<designacao>")
def conceito(designacao):
    designacao_lower = designacao.lower()
    for chave in db.keys():
        if chave.lower() == designacao_lower:
            return render_template("conceito.html", designacao=chave, descricao=db[chave])
            
    return render_template("error.html", erro=f"O conceito '{designacao}' não existe.")


app.run(host="localhost", port=4002, debug=True)