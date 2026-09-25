from pydantic import BaseModel

class ErroSchema(BaseModel):
    """ 
    Representa uma mensagem de erro
    """
    Erro: str = "Erro ao processar sua requisição"