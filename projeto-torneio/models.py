from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Jogador(Base):
    __tablename__ = "jogadores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    genero = Column(String, nullable=False)

class Torneio(Base):
    __tablename__ = "torneios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_inicio = Column(DateTime, default=datetime.datetime.utcnow)
    jogo_id = Column(Integer, ForeignKey("jogos.id"))
    jogo = relationship("Jogo")

class Partida(Base):
    __tablename__ = "partidas"
    id = Column(Integer, primary_key=True, index=True)
    torneio_id = Column(Integer, ForeignKey("torneios.id"))
    jogador1_id = Column(Integer, ForeignKey("jogadores.id"))
    jogador2_id = Column(Integer, ForeignKey("jogadores.id"))
    vencedor_id = Column(Integer, ForeignKey("jogadores.id"))

    torneio = relationship("Torneio")
    jogador1 = relationship("Jogador", foreign_keys=[jogador1_id])
    jogador2 = relationship("Jogador", foreign_keys=[jogador2_id])
    vencedor = relationship("Jogador", foreign_keys=[vencedor_id])
