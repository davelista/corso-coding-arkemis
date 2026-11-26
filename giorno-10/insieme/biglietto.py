"""IL BIGLIETTO · lo scriviamo insieme, dal vivo.

Si prova con:  python3 biglietto.py
"""

from datetime import datetime, timedelta, timezone
import jwt

SECRET_KEY="chiave_super_segreta"

def crea_jwt(utente_id: int) -> str:
    scadenza = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {"sub": str(utente_id), "exp": scadenza} # Subject, Expiration
    token_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token_jwt

mio_token = crea_jwt(1)
print("token generato: ", mio_token)
controllo = jwt.decode(mio_token, SECRET_KEY, algorithms=[HS256])
print("controllo: ", controllo)

adesso = datetime.now(timezone.utc)
token_falso = jwt.encode({"sub": "2", "exp": adesso + timedelta(minutes=30)}, SECRET_KEY_SBAGLIATA, algorithm="HS256")
token_falso_utente = jwt.encode({"sub": "1", "exp": adesso + timedelta(minutes=20)}, SECRET_KEY, algorithm="HS256")
token_scaduto = jwt.encode({"sub": "1", "exp": adesso + timedelta(minutes=30)}, SECRET_KEY, algorithm="HS256")

try:
    controllo_falso = jwt.decode(token_falso, SECRET_KEY, algorithms=["HS256"])
except:
    print("Il token è falso")

# Invece che fare il decode:
# controllo_falso_utente = jwt.decode(token_falso_utente_1, SECRET_KEY, algorithms=["HS256"])
# Confronto i due token:

controllo_token_utente = jwt.decode(mio_token, SECRET_KEY, algorithms=["HS256"])
controllo_token_falso_utente = jwt.decode(token_falso_utente, SECRET_KEY, algorithms=["HS256"])

if mio_token == token_falso_utente:
    print("Il token è corretto")
else:
    print("Il token è falso")

try:
    controllo_scaduto = jwt.decode(token_scaduto, SECRET_KEY, algorithms=["HS256"])
except:
    print("Il token è scaduto")

