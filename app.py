from flask import Flask, request, jsonify

from extensions import db
from modelos.itens_colecionaveis import ItensColecionaveis
from modelos.tipos_item import TipoItemColecionavel

app = Flask(__name__)

# Configuração do SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o aplicativo
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/cadastrar/tipos", methods=['POST'])
def cadastrar_tipos():
    dados = request.get_json()

    texto_tipo = dados.get("tipo_item")

    if not texto_tipo:
        return jsonify({"Erro":"Tipo é obrigatório"}), 400 

    try:
        novo_tipo = TipoItemColecionavel(
            tipo_item = dados.get("tipo_item")
        )

        stmt = db.select(TipoItemColecionavel).filter_by(tipo_item=texto_tipo)

        tipo_existente = db.session.execute(stmt).scalar_one_or_none()
        if tipo_existente:
            return jsonify({"Erro":"Tipo já cadastrado"}), 400

        db.session.add(novo_tipo)
        db.session.commit()

        return jsonify({"mensagem":"Tipo cadastrado com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"Erro ao cadastrar tipo": str(e)}), 400

@app.route("/consultar/tipos", methods=['GET'])
def consultar_tipos():
    try:
        tipos_itens = db.session.execute(db.select(TipoItemColecionavel).order_by(TipoItemColecionavel.id_item)).scalars().all()

        resultado = [
            {"id_item": tipo.id_item, "tipo_item": tipo.tipo_item}
            for tipo in tipos_itens
        ]
        return jsonify(resultado), 200
    
    except Exception as e:
        return jsonify({"Erro ao recuperar os tipos": str(e)}), 400