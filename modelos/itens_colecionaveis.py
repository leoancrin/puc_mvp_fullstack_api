from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from extensions import db

class ItensColecionaveis(db.Model):
    __tablename__ = 'itens_colecionaveis'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo = mapped_column(ForeignKey("tipo_item_colecionavel.id_item"))
    nome_item: Mapped[str] = mapped_column(String(50), nullable=False, default="Nome não definido")
    valor_item: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)

