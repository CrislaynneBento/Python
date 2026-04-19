from pydantic import BaseModel
from datetime import date

class sale(BaseModel):
    sale_date : date
    product_id : str 
    quantify : int 
    total_value : float