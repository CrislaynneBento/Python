from pydantic import BaseModel
from typing import Optional

#Dentro dela, vamos definir os nossos modelos de dados. 
class Product(BaseModel):

    """
    Modelo de dados para um Produto.
    """
    
    name : str
    price : float
    description : Optional[str] = None #permite que a descrição seja opcional
    stock : int

