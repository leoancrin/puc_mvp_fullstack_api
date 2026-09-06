from pydantic import BaseModel

class ErroSchema(BaseModel):
    """ 
    Representa uma mensagem de erro
    """
    mensagem: str