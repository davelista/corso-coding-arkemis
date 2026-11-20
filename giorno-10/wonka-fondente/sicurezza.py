"""La sicurezza della fabbrica · FONDENTE: le quattro funzioni le scrivete voi.

Stamattina le abbiamo costruite insieme (cartella insieme/). Ora, da soli, nell'ordine:

    F1  calcola_hash, password_giusta     pytest -v -k fondente_1
    F2  crea_biglietto                     pytest -v -k fondente_2
    F3  bambino_corrente                   pytest -v -k livello_3

Al posto dei tre puntini, il corpo della funzione. Il resto (import, password_hash,
la chiave dal .env, ALGORITMO, DURATA, il controllore HTTPBearer) è già scritto.
"""
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from database import get_db
from modelli import BambinoDB

# ============================================================ F1 · LE PASSWORD
# recommended(): argon2, con le impostazioni sicure. Il sale lo mette lui.
password_hash = PasswordHash.recommended()


def calcola_hash(password: str) -> str:
    """Dalla password, l'impronta.

    Indizio: password_hash ha un metodo che fa proprio questo. Si chiama come l'hash di stamattina.
    """
    ...


def password_giusta(password: str, impronta: str) -> bool:
    """True se la password è quella dell'impronta, False se no.

    Indizio: l'altro metodo di password_hash, quello che «verifica».
    """
    ...


# ============================================================ F2 · IL BIGLIETTO D'ORO
# La chiave segreta sta nel file .env (mai nel codice, mai su GitHub). Vedi il README.
load_dotenv(Path(__file__).parent / ".env")
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("Manca SECRET_KEY: create il file .env (README, «Una volta sola»)")

ALGORITMO = "HS256"
DURATA = timedelta(minutes=30)


def crea_biglietto(bambino_id: int) -> str:
    """Un JWT firmato, con dentro due cose:
        "sub": l'id del bambino, scritto come testo
        "exp": adesso (in UTC) + DURATA

    Indizi: è insieme/biglietto.py. Qui la chiave è SECRET_KEY e l'algoritmo è ALGORITMO.
    """
    ...


# ============================================================ F3 · IL CONTROLLORE ALL'INGRESSO
# Legge l'header «Authorization: Bearer <biglietto>». Su /docs compare il lucchetto Authorize.
controllore = HTTPBearer(auto_error=False)


def bambino_corrente(header: HTTPAuthorizationCredentials | None = Depends(controllore),
                     db: Session = Depends(get_db)) -> BambinoDB:
    """Dal biglietto al bambino.

    - Niente biglietto (header è None)                  -> 401 "Manca il biglietto"
    - Biglietto falso o scaduto (jwt.InvalidTokenError)  -> 401 "Biglietto non valido"
    - Il bambino di "sub" non c'è nel database           -> 401 "Biglietto non valido"
    - Altrimenti                                         -> return il bambino

    Indizi: è insieme/main.py. Il biglietto è in header.credentials.
    Al posto del dizionario BAMBINI: db.get(BambinoDB, ...), come ieri.
    """
    ...
