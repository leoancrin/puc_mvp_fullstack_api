from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from base import Base

class TipoItemColecionavel (Base):
    __tablename__ = 'tipo_item_colecionavel'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo_item = mapped_column(String(30), nullable=False, default="Sem classificação")

