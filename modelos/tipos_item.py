from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from extensions import db

class TipoItemColecionavel (db.Model):
    __tablename__ = 'tipo_item_colecionavel'

    id_item = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo_item = mapped_column(String(30), nullable=False, default="Sem classificação")

