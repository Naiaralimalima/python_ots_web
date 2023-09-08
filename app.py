#importar o flask pip install flask
#importar o requerimrntopip freeze> requeriments.txt 

from flask import Flask,render_template

app = Flask("ola mundo")
#lista de postagem mock
post = [
    {
    "titulo":"minha primeira postagem",
    "texto":"teste"
    },
    {
        "titulo":"segundo post",
        "texto":"outro teste"
    }
    ]
#rota
@app.route('/')
def exibir_entradas():
    entradas = post #mock das postagens 
    return render_template('exibir_entradas.html', entradas=entradas)

 