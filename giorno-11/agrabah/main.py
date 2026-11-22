"""LA LAMPADA DI AGRABAH · le quattro porte della città.

Avvio (dalla cartella agrabah, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs
Test di un livello (in un secondo terminale):
    pytest -v -k livello_0

Qui c'è solo l'app. Gli import, gli stampi e le rotte li scrivete voi: le consegne sono nel README.
"""
from fastapi import FastAPI

app = FastAPI(title="La lampada di Agrabah")
