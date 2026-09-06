from pydantic import BaseModel, Field

class TipoItemBodyCompleto(BaseModel):
    """ 
        Definição do body completo de uma requisição
    """
    id_tipo: int = Field(..., description="ID de identificação")
    tipo_item: str = Field(..., min_length=1, max_length=30, description="Nome do tipo")

class TipoItemBodySomenteTipoItem(BaseModel):
    """ 
        Definição do body de uma requisição somente com o tipo de item
    """
    tipo_item: str = Field(..., min_length=1, max_length=30, description="Nome do tipo")

