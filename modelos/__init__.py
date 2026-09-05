from sqlalchemy_utils import database_exists, create_database

from modelos.tipos_item import TipoItemColecionavel
from modelos.itens_colecionaveis import ItensColecionaveis

def init_db(app):
    """Função para inicializar o banco de dados usando a configuração do app Flask"""
    
    # Pega a URL do banco que está configurada no app.py
    db_url = app.config["SQLALCHEMY_DATABASE_URI"]
    
    # Cria o banco se ele não existir
    if not database_exists(db_url):
        create_database(db_url)
        
