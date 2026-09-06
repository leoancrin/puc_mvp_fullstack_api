from pydantic import BaseModel
from typing import Optional, List

class TipoItemSchema(BaseModel):
    """ 
        Representa um tipo de item no banco de dados
    """
    id_tipo: int = 1
    tipo_item: str = "Quadrinhos"

class ListTipoItemSchema(BaseModel):
    """ 
        Representa a lista retornada para os tipos de itens cadastrados
    """
    tipos:List[TipoItemSchema]

class AtualizaTipoItemSchema(BaseModel):
    """ 
        Representa o retorno da atualização de um tipo de item
    """
    id_tipo: int = 1
    tipo_item: str = "Quadrinhos"
    mensagem: str

class DeletaTipoItemSchema(BaseModel):
    """ 
        Representa o retorno da deleção de um tipo de item
    """
    tipo_item: str = "Quadrinhos"
    mensagem: str    