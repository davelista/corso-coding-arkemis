"""La sicurezza della fabbrica. QUESTO FILE NON SI TOCCA: si legge, riga per riga, nelle slide.

Quattro strumenti, già pronti:

    calcola_hash(password)                  la password diventa un'impronta (registrazione)
    password_giusta(password, impronta)     True se la password è quella dell'impronta (login)
    crea_biglietto(bambino_id)              il biglietto d'oro: un token JWT firmato (login)
    bambino_corrente                        il controllore all'ingresso: si usa con Depends
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

# ============================================================ LE PASSWORD
# recommended(): argon2, con le impostazioni sicure scelte da chi ne sa.
password_hash = PasswordHash.recommended()


def calcola_hash(password: str) -> str:
    """Dalla password, l'impronta. Ogni volta diversa: c'è il sale."""
    return password_hash.hash(password)


def password_giusta(password: str, impronta: str) -> bool:
    """Rifà il calcolo con il sale scritto nell'impronta, e confronta."""
    return password_hash.verify(password, impronta)


# ============================================================ IL BIGLIETTO D'ORO
# La chiave segreta sta nel file .env (mai nel codice, mai su GitHub). Vedi il README.
load_dotenv(Path(__file__).parent / ".env")
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("Manca SECRET_KEY: create il file .env (README, «Una volta sola»)")

ALGORITMO = "HS256"
DURATA = timedelta(minutes=30)


def crea_biglietto(bambino_id: int) -> str:
    """Un JWT con dentro chi è (sub) e quando scade (exp), firmato con la chiave segreta."""
    scadenza = datetime.now(timezone.utc) + DURATA
    dati = {"sub": str(bambino_id), "exp": scadenza}
    return jwt.encode(dati, SECRET_KEY, algorithm=ALGORITMO)


# ============================================================ IL CONTROLLORE ALL'INGRESSO
# Legge l'header «Authorization: Bearer <biglietto>».
# Su /docs compare il lucchetto Authorize: lì si incolla il biglietto.
controllore = HTTPBearer(auto_error=False)


def bambino_corrente(header: HTTPAuthorizationCredentials | None = Depends(controllore),
                     db: Session = Depends(get_db)) -> BambinoDB:
    """Dal biglietto al bambino. Niente biglietto, biglietto falso o scaduto, bambino sparito: 401."""
    if header is None:
        raise HTTPException(status_code=401, detail="Manca il biglietto")
    try:
        dati = jwt.decode(header.credentials, SECRET_KEY, algorithms=[ALGORITMO])   # firma e scadenza
        bambino = db.get(BambinoDB, int(dati["sub"]))
    except jwt.InvalidTokenError:
        bambino = None
    if bambino is None:
        raise HTTPException(status_code=401, detail="Biglietto non valido")
    return bambino
