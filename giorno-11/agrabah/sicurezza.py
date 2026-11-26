"""La sicurezza di Agrabah. QUESTO FILE È VUOTO: lo scrivete voi, import compresi.

Cosa ci va, livello per livello:

    Livello 2   CHIAVE_CAVERNA, letta dal file .env
                controlla_chiave        il controllore dell'header X-API-Key

    Livello 3   calcola_hash            dalla password, l'impronta
                password_giusta         la password è quella dell'impronta?

    Livello 4   SECRET_KEY, letta dal file .env
                crea_token              il token JWT: sub e exp
                padrone_corrente        dal token al padrone, con Depends

I nomi contano: i test e main.py cercano proprio questi.
Le avete già scritte tutte venerdì, con altri nomi: riaprite giorno-10 (la tabella è nel README).
"""

import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt
from dotenv import load_dotenv
from fastapi import Depends, Header, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from database import get_db
from modelli import PadroneDB

# ============================================================ LIVELLO 2:LA CHIAVE DELLA CAVERNA
load_dotenv(Path(__file__).parent / ".env")
CHIAVE_CAVERNA = os.environ.get("CHIAVE_CAVERNA")
if not CHIAVE_CAVERNA:
    raise RuntimeError("Manca CHIAVE_CAVERNA: create il file .env")

def controlla_chiave(api_key: str | None = Header(default=None, alias="X-API-Key")) -> None:
    if api_key is None:
        raise HTTPException(status_code=401, detail="Manca la chiave")
    if api_key != CHIAVE_CAVERNA:
        raise HTTPException(status_code=401, detail="Chiave sbagliata")

# ============================================================ LIVELLO 3: LE PASSWORD
password_hash = PasswordHash.recommended()

def calcola_hash(password: str) -> str:
    """Dalla password, l'impronta. Ogni volta diversa: c'è il sale."""
    return password_hash.hash(password)

def password_giusta(password: str, impronta: str) -> bool:
    """Rifà il calcolo con il sale scritto nell'impronta, e confronta."""
    return password_hash.verify(password, impronta)

# ============================================================ LIVELLO 4 · IL TOKEN JWT
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("Manca SECRET_KEY: aggiungetela al file .env")

ALGORITMO = "HS256"
DURATA = timedelta(minutes=30)

def crea_token(padrone_id: int) -> str:
    """Crea un JWT con sub (id del padrone come stringa) ed exp (scadenza a 30 minuti)."""
    scadenza = datetime.now(timezone.utc) + DURATA
    dati = {"sub": str(padrone_id), "exp": scadenza}
    return jwt.encode(dati, SECRET_KEY, algorithm=ALGORITMO)

controllore_token = HTTPBearer(auto_error=False)

def padrone_corrente(header: HTTPAuthorizationCredentials | None = Depends(controllore_token), db: Session = Depends(get_db)) -> PadroneDB:
    """Legge il token Bearer, lo verifica e restituisce il PadroneDB dal database."""
    if header is None:
        raise HTTPException(status_code=401, detail="Manca il token")
    try:
        dati = jwt.decode(header.credentials, SECRET_KEY, algorithms=[ALGORITMO])
        padrone = db.get(PadroneDB, int(dati["sub"]))
    except jwt.InvalidTokenError:
        padrone = None
    if padrone is None:
        raise HTTPException(status_code=401, detail="Token non valido")
    return padrone