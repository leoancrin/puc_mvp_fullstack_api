from sqlalchemy import Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from extensions import db
from decimal import Decimal

class ItensColecionaveis(db.Model):
    __tablename__ = 'itens_colecionaveis'

    id_item: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tipo: Mapped[int] = mapped_column(ForeignKey("tipo_item_colecionavel.id_tipo"))
    nome_item: Mapped[str] = mapped_column(String(50), nullable=False, default="Nome não definido")
    valor_item: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2), nullable=False, default=0.00)

