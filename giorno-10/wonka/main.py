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
# Indizi:
# - È la POST dell'ospite della villa (ieri): stesse mosse di SQLAlchemy.
# - Nel database va l'impronta, non la password. In sicurezza.py c'è la funzione che la calcola.
# - Nella tabella il campo si chiama password_hash (guardate modelli.py).

@app.post("/registra_bambino", status_code=status.HTTP_201_CREATED)
def registra_bambino(body: BambinoNuovo, db: Session = Depends(get_db)) -> Bambino:
    nuovo_bambino = BambinoDB(username=body.username, nome=body.nome, password_hash=calcola_hash(body.password))
    db.add(nuovo_bambino)
    db.commit()
    db.refresh(nuovo_bambino)
    bambino_creato = Bambino(id=nuovo_bambino.id, username=nuovo_bambino.username, nome=nuovo_bambino.nome)
    return bambino_creato

# ============================================================ LIVELLO 2 · IL BIGLIETTO D'ORO
# POST /login, con il corpo di Credenziali (username e password, in JSON) -> il Biglietto
# Username che non c'è, o password sbagliata -> 401 "Username o password sbagliati"
#
# Indizi:
# - Cercare per username non è db.get (db.get cerca per id): serve select … where, e poi una riga sola.
# - In sicurezza.py: una funzione controlla la password, un'altra crea il biglietto.
# - La risposta è uno stampo Biglietto: access_token e token_type (che vale "bearer").

@app.post("/login", status_code=status.HTTP_201_CREATED)
def login(body: Credenziali, db: Session=Depends(get_db)) -> Biglietto:
    bambino = db.scalar(select(BambinoDB).where(BambinoDB.username == body.username))

    if bambino is None or not password_giusta(body.password, bambino.password_hash):
        raise HTTPException(status_code=401, detail="User o password errata")

    nuovo_biglietto = Biglietto(access_token=crea_biglietto(bambino.id), token_type="bearer")

    return nuovo_biglietto

# ============================================================ LIVELLO 3 · CHI SONO?
# GET /me -> 200 e il Bambino del biglietto. Senza biglietto, o con un biglietto falso: 401.
#
# Indizi:
# - Il biglietto lo controlla il controllore di sicurezza.py: lo chiedete con Depends, nel def.
# - Il 401 non lo scrivete voi.

@app.get("/me")
def leggi_info(db: Session=Depends(get_db)) -> Bambino:
    bambino = bambino_corrente(db)
    return Bambino(id=bambino.id, username=bambino.username, nome=bambino.nome)


# ============================================================ LIVELLO 4 · LE SALE
# GET /sale/{sala_id} -> 200 e la Sala, con l'ingrediente. Solo con il biglietto: senza, 401.
# Sala che non esiste -> 404 "Sala non trovata"
#
# Indizio: è il livello 1 della villa (ieri), più il controllore del livello 3.

@app.get("/sale/{sala_id}")
def leggi_sala(sala_id: int, db: Session = Depends(get_db), bambino: BambinoDB = Depends(bambino_corrente)) -> Sala:
    sala = db.get(SalaDB, sala_id)
    if bambino is None:
        raise HTTPException(status_code=401, detail="Biglietto non valito")
    if sala is None:
        raise HTTPException(status_code=404, detail="Sala non trovata")
    return Sala(id=sala.id, nome=sala.nome, descrizione=sala.descrizione, ingrediente=sala.ingrediente)

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
