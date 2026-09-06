from flask import Flask

from extensions import db

from metodos.metodos_tipo_item import *

app = Flask(__name__)

# Configuração do SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o aplicativo
db.init_app(app)

# Inicia o banco de dados
with app.app_context():
    db.create_all()
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Rotas relacionadas aos tipos de itens
@app.route("/cadastrar/tipos", methods=['POST'])
def cadastrar_tipos():
    return metodo_cadastrar_tipos()

@app.route("/consultar/tipos", methods=['GET'])
def consultar_tipos():
    return metodo_consultar_tipos()

@app.route("/alterar/tipos", methods=['PUT'])
def alterar_tipos():
    return metodo_alterar_tipos() 

@app.route("/deletar/tipos", methods=['DELETE'])
def deletar_tipos():
    return metodo_deletar_tipos() 

# Rotas relacionadas aos itens 
@app.route("/cadastrar/itens", methods=['POST'])
def cadastrar_itens():
    return "<p>Cadastrar itens ainda não implementado!</p>"

@app.route("/consultar/itens", methods=['GET'])
def consultar_itens():
    return "<p>Consultar itens ainda não implementado!</p>"

@app.route("/alterar/itens", methods=['PUT'])
def alterar_itens():
    return "<p>Alterar itens ainda não implementado!</p>"

@app.route("/deletar/itens", methods=['DELETE'])
def deletar_itens():
    return "<p>Deletar itens ainda não implementado!</p>"