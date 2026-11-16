"""L'API della flotta: le navi dei Caraibi, salvate in memoria.

Avvio (dalla cartella flotta, con il venv acceso):
    fastapi dev main.py        poi aprite http://127.0.0.1:8000/docs
Test (in un secondo terminale):
    pytest -v
"""
from itertools import count
from typing import Literal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="L'API della flotta")

# Le quattro bandiere ammesse: le stesse del CHECK nella tabella navi del giorno 5.
Bandiera = Literal["pirata", "Marina", "Compagnia delle Indie", "mercantile"]


class NaveNuova(BaseModel):
    """Quello che il client manda: tutto tranne l'id."""
    nome: str = Field(min_length=1, max_length=50)
    capitano: str = Field(min_length=1, max_length=50)
    bandiera: Bandiera
    cannoni: int = Field(ge=0, le=200)
    porto_base: str | None = None  # alcune navi non tornano mai in porto


class Nave(NaveNuova):
    """Quello che il server restituisce: con l'id."""
    id: int


# I dati vivono qui finché il server è acceso. Domani: il database pirati.
flotta: dict[int, Nave] = {}
contatore = count(1)


def trova(nave_id: int) -> Nave:
    nave = flotta.get(nave_id)
    if nave is None:
        raise HTTPException(status_code=404, detail="Nave non trovata")
    return nave


# ------------------------------------------------ già fatte insieme
@app.get("/navi")
def lista_navi(bandiera: Bandiera | None = None, min_cannoni: int | None = None) -> list[Nave]:
    # EXTRA: usate bandiera e min_cannoni per filtrare la lista
    return list(flotta.values())


@app.get("/navi/{nave_id}")
def leggi_nave(nave_id: int) -> Nave:
    return trova(nave_id)


@app.post("/navi", status_code=status.HTTP_201_CREATED)
def crea_nave(dati: NaveNuova) -> Nave:
    # EXTRA: se il nome è già usato da un'altra nave, rispondete 409 "Nome già usato"
    for id_nave in flotta:
        nave = flotta[id_nave]
        if nave.nome == dati.nome:
            raise HTTPException(status_code=409, detail="Nome già usato")
    nave = Nave(id=next(contatore), **dati.model_dump())
    flotta[nave.id] = nave
    return nave


# ------------------------------------------------ OBBLIGATORIO: tocca a voi
# PUT /navi/{nave_id}     -> sostituisce la nave con i dati nuovi, risponde 200 con la nave
#                            404 "Nave non trovata" se non esiste
# DELETE /navi/{nave_id}  -> affonda la nave, risponde 204 senza corpo
#                            404 "Nave non trovata" se non esiste
@app.put("/navi/{nave_id}")
def aggiorna_nave(nave_id: int, dati: NaveNuova) -> Nave:
    nave = trova(nave_id)
    nave = Nave(id=nave_id, **dati.model_dump())
    flotta[nave_id] = nave
    return nave

@app.delete("/navi/{nave_id}", status_code=204)
def affonda_nave(nave_id: int) -> None:
    trova(nave_id)
    flotta.pop(nave_id)


# ------------------------------------------------ la flotta di partenza (la stessa del database pirati)
NAVI_DI_PARTENZA = [
    ("Perla Nera", "Jack Sparrow", "pirata", 32, "Tortuga"),
    ("Olandese Volante", "Davy Jones", "pirata", 46, None),
    ("Queen Anne's Revenge", "Barbanera", "pirata", 40, "Nassau"),
    ("Dauntless", "James Norrington", "Marina", 50, "Port Royal"),
    ("Endeavour", "Cutler Beckett", "Compagnia delle Indie", 60, "Port Royal"),
    ("Empress", "Sao Feng", "pirata", 24, "Singapore"),
    ("Silent Mary", "Armando Salazar", "Marina", 38, None),
    ("Providence", "Hector Barbossa", "Marina", 30, "Londra"),
    ("Edinburgh Trader", "Capitano Bellamy", "mercantile", 12, "Tortuga"),
]

for nome, capitano, bandiera, cannoni, porto_base in NAVI_DI_PARTENZA:
    crea_nave(NaveNuova(nome=nome, capitano=capitano, bandiera=bandiera, cannoni=cannoni, porto_base=porto_base))
