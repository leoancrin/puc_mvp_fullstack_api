from flask_openapi3 import Info, OpenAPI, Tag

from extensions import db

from metodos.metodos_tipo_item import *

from schemas.tipos_item_schema import *
from schemas.error import *

from requisicao.tipo_item_requests import *

info = Info(title='API de itens colecionáveis', version='1.0.0')
app = OpenAPI(__name__, info=info)

# Configuração do SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o aplicativo
db.init_app(app)

# Inicia o banco de dados
with app.app_context():
    db.create_all()

# tags
tipo_item_tag = Tag(name="Tipo de item colecionável", description="Realiza CRUD para os tipos de itens colecionáveis na base de dados")
item_colecionavel_tag = Tag(name="Itens colecionáveis", description="Realiza CRUD para os itens colecionáveis na base de dados")    
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Rotas relacionadas aos tipos de itens
@app.post('/cadastrar/tipos', tags=[tipo_item_tag], 
          responses={
              200: TipoItemSchema,
              400: ErroSchema,
              409: ErroSchema
          })
def cadastrar_tipos(body: TipoItemBodySomenteTipoItem):
    """
        Cadastra um tipo de item colecionável
    """
    return metodo_cadastrar_tipos()

@app.get('/consultar/tipos', tags=[tipo_item_tag],
         responses={
             200: ListTipoItemSchema,
             400: ErroSchema
         })
def consultar_tipos():
    """
        Consulta todos os tipos de itens cadastrados
    """
    return metodo_consultar_tipos()

@app.put('/alterar/tipos', tags=[tipo_item_tag],
         responses={
             200: AtualizaTipoItemSchema,
             400: ErroSchema,
             422: ErroSchema
         })
def alterar_tipos(body: TipoItemBodyCompleto):
    """
        Altera um tipo de item cadastrado anteriormente
    """
    return metodo_alterar_tipos() 

@app.delete('/deletar/tipos', tags=[tipo_item_tag],
            responses={
                200: DeletaTipoItemSchema,
                400: ErroSchema,
                404: ErroSchema,
                409: ErroSchema
            })
def deletar_tipos(body: TipoItemBodyCompleto):
    """
        Deleta um tipo de item colecionável cadastrado na base
    """
    return metodo_deletar_tipos() 

# Rotas relacionadas aos itens 
@app.post('/cadastrar/itens', tags=[item_colecionavel_tag])
def cadastrar_itens():
    """
        Cadastra um item colecionável
    """
    return "<p>Cadastrar itens ainda não implementado!</p>"

@app.get('/consultar/itens', tags=[item_colecionavel_tag])
def consultar_itens():
    """
        Consulta todos os item colecionáveis existentes
    """
    return "<p>Consultar itens ainda não implementado!</p>"

@app.put('/alterar/itens', tags=[item_colecionavel_tag])
def alterar_itens():
    """
        Altera um item colecionável cadastrado anteriormente
    """
    return "<p>Alterar itens ainda não implementado!</p>"

@app.delete('/deletar/itens', tags=[item_colecionavel_tag])
def deletar_itens():
    """
        Deleta item colecionável cadastrado
    """
    return "<p>Deletar itens ainda não implementado!</p>"