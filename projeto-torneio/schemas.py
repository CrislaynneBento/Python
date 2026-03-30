from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class JogadorBase(BaseModel):
    nome : str
    nickname: str
    email: EmailStr

class JogadorCreate(JogadorBase):
    pass 

class JogadorResponse(JogadorBase):
    id: int
    class Config:
        from_attributes = True
    
class JogoBase(BaseModel):
    nome: str
    genero: str

class JogoCreate(JogoBase):
    pass

class JogoResponse(JogoBase):
    id: int
    class Config:
        from_attributes = True

class TorneioBase(BaseModel):
    nome: str
    jogo_id: int

class TorneioCreate(TorneioBase):
    pass

class TorneioResponse(TorneioBase):
    id: int
    data_inicio: datetime
    class Config:
        from_attributes = True

class PartidaBase(BaseModel):
    torneio_id: int
    jogador1_id: int
    jogador2_id: int
    vencedor_id: Optional[int] = None

class PartidaCreate(PartidaBase):
    pass

class PartidaResponse(PartidaBase):
    id: int
    class Config:
        from_attributes = True

