from flask import Flask, request, jsonify

from extensions import db
from modelos.itens_colecionaveis import ItensColecionaveis
from modelos.tipos_item import TipoItemColecionavel

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
    
# Rotas
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

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