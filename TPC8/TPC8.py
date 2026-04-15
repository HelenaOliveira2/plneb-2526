from flask import Flask, render_template, request
import json
import re
import random

app = Flask(__name__)

f_db=open("C:\\Users\\helen\\Desktop\\Mestrado\\2Semestre\\PLN\\plneb-2526\\TPC7\\dicionario_medico.json", "r", encoding="utf-8")
db = json.load(f_db)


@app.get("/")
def home_page():
    primeiros_conceitos = random.sample(list(db.keys()), 6)
    return render_template("home.html", conceitos=primeiros_conceitos)


@app.get("/conceitos")
def listar_conceitos():
    return render_template("conceitos.html", conceitos = db.keys())

@app.get("/conceitos/<designacao>")
def conceito(designacao):
    if designacao in db:
        descricao = db[designacao]
        return render_template("conceito.html", designacao = designacao, descricao = descricao)
    else:
        return render_template("erro.html", erro = "O conceito introduzido não existe")

@app.get("/api/conceitos")
def conceitos_api():
    return db

@app.post("/conceitos")
def adicionar_conceitos():
    descricao = request.form["descricao"]
    designacao = request.form["designacao"]
    db[designacao] = descricao
    f_out=open("bd.json","w")
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return render_template("conceitos.html", conceitos=db.keys())

@app.delete("/conceitos/<designacao>")
def apagar_conceito(designacao):
    del db[designacao]
    f_out=open("bd.json","w")
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return {"redirect_url": "/conceitos", "message":"Conceito apagado com sucesso"}

@app.get("/tabela")
def tabela():
    return render_template("tabela.html", conceitos=db)

@app.get("/pesquisar")
def pesquisar():
    termo = request.args.get("termo", "")
    exata = request.args.get("exata") 
    maiusculas = request.args.get("maiusculas") 

    resultados = {}

    if termo:
        flags = 0 if maiusculas else re.IGNORECASE

        if exata:
            pattern = rf"\b({re.escape(termo)})\b"
        else:
            pattern = rf"({re.escape(termo)})"

        for designacao, descricao in db.items():
            if re.search(pattern, designacao, flags) or re.search(pattern, descricao, flags):
                desig_destacada = re.sub(pattern, r"<b>\1</b>", designacao, flags=flags)
                desc_destacada = re.sub(pattern, r"<b>\1</b>", descricao, flags=flags)
                resultados[desig_destacada] = desc_destacada

    return render_template("pesquisar.html", resultados=resultados, termo=termo)


app.run(host="localhost", port=4002, debug=True)