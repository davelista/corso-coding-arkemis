"""IL MAGAZZINO DI WONKA · la chiave dei fornitori.

Il magazzino non lo usa una persona: lo usa il programma del fornitore di cacao.
Un programma non fa il login. Mostra una chiave (API Key) in un header, a ogni richiesta:

    X-API-Key: 9f2c4e7a...

Avvio (dalla cartella chiave, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs
I test (in un secondo terminale):
    pytest -v

Si tocca SOLO questo file.
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException

# ============================================================ LA CHIAVE GIUSTA (già fatto)
# La chiave giusta sta nel file .env, mai nel codice e mai su GitHub (README, «Una volta sola»).
load_dotenv(Path(__file__).parent / ".env")
CHIAVE_MAGAZZINO = os.environ.get("CHIAVE_MAGAZZINO")
if not CHIAVE_MAGAZZINO:
    raise RuntimeError("Manca CHIAVE_MAGAZZINO: create il file .env (README, «Una volta sola»)")

FORNITORE = "Cacao del Loompaland"      # a chi abbiamo dato la chiave

app = FastAPI(title="Il magazzino di Wonka")

# Il magazzino è un dizionario: chiave = ingrediente, valore = kg.
MAGAZZINO = {"cacao": 120, "zucchero": 300, "nocciole": 45}


# ============================================================ L'ESEMPIO (già fatto)
# GET /: la porta d'ingresso, per tutti. Niente chiave.

@app.get("/")
def ingresso() -> dict:
    return {"messaggio": "Il magazzino di Wonka. Per entrare serve la chiave."}


# ============================================================ IL CONTROLLORE · lo scriviamo insieme
# 1. Il controllore. È una funzione, NON una rotta: niente @app.
#    Il valore dell'header X-API-Key arriva nel parametro chiave (già scritto qui sotto).
#    Al posto dei tre puntini:
#      - chiave è None (l'header non c'è)       -> 401 "Manca la chiave"
#      - chiave è diversa da CHIAVE_MAGAZZINO   -> 401 "Chiave sbagliata"
#      - altrimenti                             -> return FORNITORE
#
# 2. Proteggete GET /magazzino: dentro le parentesi del def, il parametro
#        fornitore: str = Depends(controlla_chiave)
#    e nella risposta, al posto di MAGAZZINO:
#        {"fornitore": fornitore, "magazzino": MAGAZZINO}

def controlla_chiave(chiave: str | None = Header(default=None, alias="X-API-Key")) -> str:
    ...


@app.get("/magazzino")
def leggi_magazzino() -> dict:
    return MAGAZZINO
