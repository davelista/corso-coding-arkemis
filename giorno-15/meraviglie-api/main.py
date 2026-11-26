"""IL PAESE DELLE MERAVIGLIE · l'API di oggi.

Avvio (dalla cartella meraviglie-api, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs

Questa API è già scritta: oggi si lavora sul frontend.
L'unica cosa da toccare è il blocco CORS qui sotto, nell'esercizio 3.
Per rimettere tutti gli ospiti come all'inizio: Ctrl+C e riaccendete l'API.
"""
import time

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Il Paese delle Meraviglie")

# ESERCIZIO 3 · CORS: togliete il # dalle sei righe qui sotto, poi salvate.
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


class Invito(BaseModel):
    invitato: bool


ospiti = {
    1: {"id": 1, "nome": "Lepre Marzolina", "specie": "Lepre", "dove": "Il tavolo lungo",
        "frase": "Buon non-compleanno! Io sono già seduta, con il burro migliore.", "invitato": True},
    2: {"id": 2, "nome": "Pinco Panco e Panco Pinco", "specie": "Gemelli", "dove": "Il bosco",
        "frase": "Veniamo, veniamo! Anzi: siamo già venuti.", "invitato": True},
    3: {"id": 3, "nome": "Ghiro", "specie": "Ghiro", "dove": "Dentro la teiera",
        "frase": "Zzz… sono a tavola… zzz…", "invitato": True},
    4: {"id": 4, "nome": "Brucaliffo", "specie": "Bruco", "dove": "Il fungo gigante",
        "frase": "Chi… sei… tu? Va bene, vengo, ma solo per il tè. La parola è CAMOMILLA.",
        "invitato": False},
    5: {"id": 5, "nome": "Stregatto", "specie": "Gatto", "dove": "Sopra un ramo",
        "frase": "Vengo. O forse sono già lì: cercate il sorriso.", "invitato": False},
    6: {"id": 6, "nome": "Dodo", "specie": "Uccello", "dove": "La spiaggia",
        "frase": "Una corsetta e arrivo! Il tè non si fredda, vero?", "invitato": False},
}

ULTIMO = "La tavola è al completo: buon non-compleanno a tutti! La parola è TEIERA."


@app.get("/")
def benvenuto():
    return {"paese": "Il Paese delle Meraviglie", "ospiti": "/ospiti"}


@app.get("/ospiti")
def elenco_ospiti():
    time.sleep(1.5)  # il Bianconiglio è sempre in ritardo: è il tempo del «sta caricando…»
    return list(ospiti.values())


@app.get("/ospiti/{ospite_id}")
def un_ospite(ospite_id: int):
    if ospite_id not in ospiti:
        raise HTTPException(status_code=404, detail="Questo ospite non è sulla lista")
    return ospiti[ospite_id]


@app.put("/ospiti/{ospite_id}")
def invita_ospite(ospite_id: int, dati: Invito):
    if ospite_id not in ospiti:
        raise HTTPException(status_code=404, detail="Questo ospite non è sulla lista")
    ospite = ospiti[ospite_id]
    era_gia_invitato = ospite["invitato"]
    ospite["invitato"] = dati.invitato
    risposta = dict(ospite)
    tutti = all(o["invitato"] for o in ospiti.values())
    if tutti and not era_gia_invitato:
        risposta["frase"] = ospite["frase"] + " " + ULTIMO
    return risposta
