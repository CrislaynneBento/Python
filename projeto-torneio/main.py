from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
import models, schemas
from database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#jogadores
@app.post("/jogadores/", response_model=schemas.JogadorResponse)
def criar_jogador(jogador: schemas.JogadorCreate, db: Session = Depends(get_db)):
    db_jogador = models.Jogador(**jogador.model_dump())
    db.add(db_jogador)
    db.commit()
    db.refresh(db_jogador)
    return db_jogador

@app.get("/jogadores/", response_model=list[schemas.JogadorResponse])
def listar_jogadores(db: Session = Depends(get_db)):
    return db.query(models.Jogador).all()

#Jogos
@app.post("/jogos/", response_model=schemas.JogoResponse)
def criar_jogo(jogo: schemas.JogoCreate, db: Session = Depends(get_db)):
    db_jogo = models.Jogo(**jogo.model_dump())
    db.add(db_jogo)
    db.commit()
    db.refresh(db_jogo)
    return db_jogo

@app.get("/jogos/", response_model=list[schemas.JogoResponse])
def listar_jogos(db: Session = Depends(get_db)):
    return db.query(models.Jogo).all()

#Torneios
@app.post("/torneios/", response_model=schemas.TorneioResponse)
def criar_torneio(torneio: schemas.TorneioCreate, db: Session = Depends(get_db)):
    db_torneio = models.Torneio(**torneio.model_dump())
    db.add(db_torneio)
    db.commit()
    db.refresh(db_torneio)
    return db_torneio

@app.get("/torneios/", responde_model=list[schemas.JogadorResponse])
def listar_torneios(db: Session = Depends(get_db)):
    return db.query(models.Torneio).all()

@app.post("/partidas/", response_model=schemas.PartidaResponse)
def criar_partida(partida: schemas.PartidaCreate, db: Session = Depends(get_db)):
    db_partidas = models.Partida(**partida.model_dump())
    db.add(db_partidas)
    db.commit()
    db.refresh(db_partidas)
    return db_partidas

@app.get("/partidas/", response_model=list[schemas.PartidaResponse])
def listar_partidas(db: Session = Depends(get_db)):
     return db.query(models.Partida).options(
        joinedload(models.Partida.torneio),
        joinedload(models.Partida.jogador1),
        joinedload(models.Partida.jogador2),
        joinedload(models.Partida.vencedor)
    ).all()