"""LA FABBRICA DI CIOCCOLATO · i cancelli di Willy Wonka.

Avvio (dalla cartella wonka, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs
Test di un livello (in un secondo terminale):
    pytest -v -k livello_1

Si tocca SOLO questo file.
"""
import hashlib

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from modelli import BambinoDB, SalaDB
from sicurezza import bambino_corrente, calcola_hash, crea_biglietto, password_giusta

app = FastAPI(title="La fabbrica di cioccolato")


# ============================================================ GLI STAMPI
class BambinoNuovo(BaseModel):          # il corpo della registrazione: la password arriva in chiaro, una volta sola
    username: str = Field(min_length=3, max_length=30)
    nome: str = Field(min_length=1)
    password: str = Field(min_length=8)


class Bambino(BaseModel):               # la risposta: niente password, niente impronta
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    nome: str


class Credenziali(BaseModel):           # il corpo del login
    username: str
    password: str


class Biglietto(BaseModel):             # la risposta del login: il biglietto d'oro
    access_token: str
    token_type: str


class SalaInVetrina(BaseModel):         # quello che vedono tutti
    model_config = ConfigDict(from_attributes=True)
    id: int
    nome: str


class Sala(SalaInVetrina):              # quello che vede solo chi ha il biglietto
    descrizione: str
    ingrediente: str


class Ricetta(BaseModel):
    parola: str


# ============================================================ L'ESEMPIO (già fatto)
# GET /sale: la vetrina, per tutti. Niente biglietto, niente ingredienti.

@app.get("/sale")
def lista_sale(db: Session = Depends(get_db)) -> list[SalaInVetrina]:
    return db.scalars(select(SalaDB).order_by(SalaDB.id)).all()


# ============================================================ LIVELLO 1 · LA REGISTRAZIONE
# POST /bambini, con il corpo di un BambinoNuovo -> 201 e il Bambino (senza password)
#
# È la POST di stamattina, con una riga nuova: al posto della password si salva l'impronta.
#     password_hash=calcola_hash(dati.password)
# Poi add, commit, refresh, return. Il 201 nel decoratore.



# ============================================================ LIVELLO 2 · IL BIGLIETTO D'ORO
# POST /login, con il corpo di Credenziali (username e password, in JSON) -> il Biglietto
# Username che non c'è, o password sbagliata -> 401 "Username o password sbagliati"
#
# Cercare un bambino per username (non per id, quindi niente db.get):
#     bambino = db.scalar(select(BambinoDB).where(BambinoDB.username == dati.username))
#
# Controllare la password:  password_giusta(dati.password, bambino.password_hash)   -> True o False
#
# Il biglietto si crea con crea_biglietto(bambino.id), e si restituisce così:
#     return Biglietto(access_token=..., token_type="bearer")



# ============================================================ LIVELLO 3 · CHI SONO?
# GET /me -> 200 e il Bambino del biglietto. Senza biglietto, o con un biglietto falso: 401.
#
# Il controllo lo fa il controllore: basta un parametro in più nel def.
#     bambino: BambinoDB = Depends(bambino_corrente)
# Il 401 lo manda lui: voi restituite il bambino, e basta.



# ============================================================ LIVELLO 4 · LE SALE
# GET /sale/{sala_id} -> 200 e la Sala, con l'ingrediente. Solo con il biglietto: senza, 401.
# Sala che non esiste -> 404 "Sala non trovata"
#
# È il livello 1 di stamattina (db.get, None, 404), più il controllore del livello 3.
# Il parametro bambino non lo usate: c'è perché il controllore lavori.



# ============================================================ IL FINALE (già fatto, non si tocca)
# Visitate le cinque sale, segnate la prima lettera di ogni ingrediente, in ordine di sala:
# è la parola segreta. Poi, con il biglietto: POST /ricetta con {"parola": "....."}
#
# La parola qui sotto non c'è: Wonka ha salvato solo la sua impronta (sha256). Come le password.
IMPRONTA_DELLA_PAROLA = "7ce76417849ffa258bc90c84b617c0b18ca45625ed8d9d3e6754e4f4bc2ad15b"


@app.post("/ricetta")
def prova_la_ricetta(ricetta: Ricetta, bambino: BambinoDB = Depends(bambino_corrente)) -> dict:
    impronta = hashlib.sha256(ricetta.parola.strip().upper().encode()).hexdigest()
    if impronta != IMPRONTA_DELLA_PAROLA:
        raise HTTPException(status_code=400, detail="La ricetta non torna: rivisitate le sale")
    return {"messaggio": f"Bravo, {bambino.nome}! La ricetta della Caramella Eterna è tua."}


# ============================================================ EXTRA: nel README
