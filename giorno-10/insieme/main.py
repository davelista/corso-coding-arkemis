"""IL CONTROLLORE · lo scriviamo insieme, dal vivo.

Si accende con:  fastapi dev main.py     poi, in Postman: GET /saluto con il biglietto
"""

import jwt
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from biglietto import SECRET_KEY

app = FastAPI(title="Esercizio: Controllore")

UTENTI = {
    1: "Asdrubale",
    2: "Davide"
}

controllo_bearer = HTTPBearer(auto_error=False)

def controllo_utente(header: HTTPAuthorizationCredentials | None = Depends(controllo_bearer)):
    if header is None:
        raise HTTPException(status_code=401, detail="Manca il codice JWT")

    try:
        # Payload {"sub": "1", "exp": "1"}
        dati = jwt.decode(header.credentials, SECRET_KEY, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=401, detail="Codice JWT non valido")

    id_che_manda_richiesta = dati["sub"] # Ci prende l'id dell'utente
    scadenza = dati["exp"] # Scadenza del jwt
    nome_utente = UTENTI.get(int(id_che_manda_richiesta))

    if nome_utente is None:
        raise HTTPException(status_code=401, detail="Codice JWT non valido")
    
    return nome_utente

@app.get("/info")
def info_utente(nome: str = Depends(controllo_utente)) -> dict:
    return {"nome": nome}
