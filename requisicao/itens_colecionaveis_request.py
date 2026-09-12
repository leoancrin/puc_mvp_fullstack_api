from pydantic import BaseModel, Field
from decimal import Decimal

class ItemColecionavelBodyCompleto(BaseModel):
    """ 
        Definição do body completo de uma requisição
    """
    id_item: int = Field(..., description="ID de identificação", json_schema_extra={"exemplo": 1})
    tipo: str = Field(..., min_length=1, max_length=30, description="Nome do tipo do item")
    nome_item: str = Field(..., min_length=1, max_length=50, description="Nome do item")
    valor_item: Decimal = Field(..., description="Valor monetário do item")

class ItemColecionavelBodyCadastro(BaseModel):
    """ 
        Definição do body de uma requisição para cadastrar um item
    """
    tipo: str = Field(..., min_length=1, max_length=30, description="Nome do tipo do item")
    nome_item: str = Field(..., min_length=1, max_length=50, description="Nome do item")
    valor_item: Decimal = Field(..., description="Valor monetário do item")

class ItemColecionavelPorTipoPath(BaseModel):
    """ 
        Definição do path de uma requisição para itens colecionáveis de um tipo específico de item
    """
    tipo_item_colecionavel: str = Field(..., min_length=1, max_length=30, description="Tipo de item específico")