from pydantic import BaseModel
from typing import List
from decimal import Decimal

class ItemColecionavelSchema(BaseModel):
    """ 
        Representa um item colecionavel no banco de dados
    """
    id_item: int = 1
    tipo: str = "Quadrinhos"
    nome_item: str = "Homem-aranha 1"
    valor_item: Decimal = 10.5    

class ListItemColecionavelSchema(BaseModel):
    """ 
        Representa a lista retornada para os itens colecionaveis cadastrados
    """
    List[ItemColecionavelSchema]

class CadastraItemColecionavelSchema(BaseModel):
    """ 
        Representa a retorno de um item cadastrado no banco
    """
    tipo: str = "Quadrinhos"
    nome_item: str = "Homem-aranha 1"
    valor_item: Decimal = 10.5
    mensagem: str = "Item cadastrado com sucesso"

class AtualizaItemColecionavelSchema(BaseModel):
    """ 
        Representa o retorno da atualização de um item colecionavel
    """
    id_item: int = 1
    tipo: str = "Quadrinhos"
    nome_item: str = "Homem-aranha 1"
    valor_item: Decimal = 10.55
    mensagem: str = "Item alterado com sucesso"

class DeletaItemColecionavelSchema(BaseModel):
    """ 
        Representa o retorno da deleção de um item colecionavel
    """
    tipo: str = "Quadrinhos"
    nome_item: str = "Homem-aranha 1"
    valor_item: Decimal = 10.5
    mensagem: str = "Item deletado com sucesso"