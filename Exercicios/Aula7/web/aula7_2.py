from flask import Flask, render_template
import json

app = Flask(__name__)

f_db=open("C:\\Users\\helen\\Desktop\\Mestrado\\2Semestre\\PLN\\plneb-2526\\Exercicios\\Aula3\\dicionario_medico.json", "r", encoding="utf-8")
db = json.load(f_db)

@app.get("/")
def home_page():
    return render_template("home.html")


@app.get("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html", conceitos=db.keys())

@app.get("/conceitos/<designacao>")
def conceito(designacao):
    if designacao in db:
        descricao=db[designacao]
        return render_template("conceito.html", designacao=designacao, descricao=descricao)
    else:
        return render_template("error.html", erro = "O conceito introduzido não existe.")


@app.get("/api/conceitos")
def conceitos_api():
    return db

app.run(host="localhost", port=4002, debug=True)


# criar home page usando bootstrap hero