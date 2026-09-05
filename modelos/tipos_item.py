from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from modelos import base

class TipoItemColecionavel (base.Base):
    __tablename__ = 'tipo_item_colecionavel'

    id_item = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo_item = mapped_column(String(30), nullable=False, default="Sem classificação")

