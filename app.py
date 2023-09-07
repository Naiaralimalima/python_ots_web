#importar o flask pip install flask
#pip freeze> requeriments.txt 

from flask import Flask

app = Flask("ola mundo")

@app.route('/')
def hello_world():
    return 'Hello, World!'

