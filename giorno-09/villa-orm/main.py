"""LA VILLA CON SQLALCHEMY · le stesse rotte di ieri, senza scrivere il SQL.

Avvio (dalla cartella villa-orm, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs
Test di un livello (in un secondo terminale):
    pytest -v -k livello_1

Si tocca SOLO questo file.
"""
from typing import Literal

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from modelli import GuardiaDB, OspiteDB, StanzaDB

app = FastAPI(title="La villa, con SQLAlchemy")


# ============================================================ GLI STAMPI DI PYDANTIC
# Gli stessi di ieri, con una riga in più nello stampo della risposta:
# from_attributes=True vuol dire «puoi leggere un oggetto con il punto» (ospite.nome),
# non solo un dizionario (ospite["nome"]). Serve perché adesso restituiamo oggetti OspiteDB.

class OspiteNuovo(BaseModel):                      # il corpo che arriva: senza id
    nome: str = Field(min_length=1)
    professione: str = Field(min_length=1)


class Ospite(OspiteNuovo):                         # la risposta che parte: con l'id
    model_config = ConfigDict(from_attributes=True)
    id: int


class GuardiaNuova(BaseModel):
    nome: str = Field(min_length=1)
    stanza_id: int
    turno: Literal["sera", "notte"]
    anni_servizio: int = Field(ge=0)


class Guardia(GuardiaNuova):
    model_config = ConfigDict(from_attributes=True)
    id: int


# ============================================================ L'ESEMPIO (già fatto)
# Ieri:  conn.execute("SELECT * FROM ospiti ORDER BY id").fetchall()
# Oggi:  la stessa domanda, scritta in Python. Il SQL lo scrive SQLAlchemy:
#        guardatelo nel terminale del server.

@app.get("/ospiti")
def lista_ospiti(db: Session = Depends(get_db)) -> list[Ospite]:
    ospiti = db.scalars(select(OspiteDB).order_by(OspiteDB.id)).all()
    return ospiti


# ============================================================ LIVELLO 1 · db.get (INSIEME)
# GET /ospiti/{ospite_id} -> 200 e l'ospite, oppure 404 "Ospite non trovato"
#
# db.get(OspiteDB, ospite_id) cerca la riga con quella chiave primaria:
# restituisce un oggetto OspiteDB, oppure None se non c'è. Come stanze.get(3) del colpo.

@app.get("/ospiti/{ospite_id}")
def leggi_ospite(ospite_id: int, db: Session = Depends(get_db)) -> Ospite:
    ospite = db.get(OspiteDB, ospite_id) 
    
    if ospite is None: 
        raise HTTPException(status_code=404, detail="Ospite non trovato")
    return ospite

# ============================================================ LIVELLO 2 · add, commit
# POST /ospiti, con il corpo di un OspiteNuovo -> 201 e l'ospite salvato, con il suo id
#
# Quattro righe, sempre le stesse:
#     ospite = OspiteDB(nome=..., professione=...)    l'oggetto nuovo: l'id ancora non c'è
#     db.add(ospite)                                  nel carrello
#     db.commit()                                     consegnato: adesso è nel database
#     db.refresh(ospite)                              riletto: adesso ha l'id
# Poi lo restituite. Il 201 va nel decoratore, come ieri.

@app.post("/ospiti", status_code=201)
def aggiungi_ospite(nuovo_ospite: OspiteNuovo, db: Session = Depends(get_db)) -> Ospite:
    ospite = OspiteDB(nome=nuovo_ospite.nome, professione=nuovo_ospite.professione)
    
    db.add(ospite)
    db.commit()
    db.refresh(ospite)
    
    return ospite
# ============================================================ LIVELLO 3 · delete
# DELETE /ospiti/{ospite_id} -> 204 senza corpo, oppure 404 "Ospite non trovato"
#
# Prima lo cercate (livello 1). Se c'è:
#     db.delete(ospite)
#     db.commit()
# Non restituite niente: il 204 va nel decoratore.

@app.delete("/ospiti/{ospite_id}", status_code=204)
def elimina_ospite(ospite_id: int, db: Session = Depends(get_db)) -> None:
    ospite = db.get(OspiteDB, ospite_id)
  
    if ospite is None: 
        raise HTTPException(status_code=404, detail="Ospite non trovato")
        
    db.delete(ospite)
    db.commit()
    
    
    

# ============================================================ LIVELLO 4 · modificare
# PUT /guardie/{guardia_id}, con il corpo di una GuardiaNuova -> 200 e la guardia aggiornata,
# oppure 404 "Guardia non trovata"
#
# Niente UPDATE da scrivere: si cerca l'oggetto, si cambiano i suoi attributi, si fa commit.
#     guardia.nome = dati.nome
#     ... (un attributo per riga, tutti e quattro)
#     db.commit()
# La sessione si accorge da sola di cosa è cambiato.


@app.put("/guardie/{guardia_id}")
def modifica_guardia(guardia_id: int, dati: GuardiaNuova, db: Session = Depends(get_db)) -> Guardia:
    guardia = db.get(GuardiaDB, guardia_id)
    if guardia is None:
        raise HTTPException(status_code=404, detail="Guardia non trovata")

    guardia.nome = dati.nome
    guardia.stanza_id = dati.stanza_id
    guardia.turno = dati.turno
    guardia.anni_servizio = dati.anni_servizio

    db.commit()
    return guardia
# ============================================================ EXTRA: nel README
