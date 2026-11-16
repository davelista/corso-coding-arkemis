"""Il primo server.

Avvio (dalla cartella giorno-06, con il venv acceso):
    fastapi dev primo-server/main.py
Poi aprite http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI

app = FastAPI(title="Il mio primo server")


@app.get("/")
def home():
    return {"messaggio": "Ahoy! Il server è acceso"}


# Un pezzo del percorso diventa un argomento della funzione:
#   GET /saluta/Anna  ->  nome = "Anna"
# Quello che sta dopo il ? diventa un altro argomento:
#   GET /saluta/Anna?volte=3  ->  volte = 3
@app.get("/saluta/{nome}")
def saluta(nome: str, volte: int = 1):
    # * volte ripete il testo, strip() toglie lo spazio in fondo
    return {"saluto": (f"Ciao {nome}! " * volte).strip()}
