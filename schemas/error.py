from pydantic import BaseModel

class ErroSchema(BaseModel):
    """ 
    Representa uma mensagem de erro
    """
    erro: str = "Erro ao processar sua requisição"