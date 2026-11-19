"""I test del magazzino. NON si modificano.

I test usano una loro chiave, non la vostra.

    pytest -v
"""
import os

os.environ["CHIAVE_MAGAZZINO"] = "chiave-solo-per-i-test"       # i test non leggono la vostra chiave

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
GIUSTA = {"X-API-Key": "chiave-solo-per-i-test"}
SBAGLIATA = {"X-API-Key": "abc123"}
COME_NUOVO = {"cacao": 120, "zucchero": 300, "nocciole": 45}


def test_esempio_ingresso():
    r = client.get("/")
    assert r.status_code == 200


# ------------------------------------------------------------ il controllore
def test_porta_senza_chiave():
    r = client.get("/magazzino")
    assert r.status_code == 401, (
        "Senza l'header X-API-Key la porta deve dire 401. "
        "Il controllore è scritto? È nel def di leggi_magazzino, con Depends?")
    assert r.json()["detail"] == "Manca la chiave"


def test_porta_chiave_sbagliata():
    r = client.get("/magazzino", headers=SBAGLIATA)
    assert r.status_code == 401, "Con la chiave sbagliata la porta deve dire 401"
    assert r.json()["detail"] == "Chiave sbagliata"


def test_porta_chiave_giusta():
    r = client.get("/magazzino", headers=GIUSTA)
    assert r.status_code == 200, (
        "Con la chiave giusta si entra. Se è 401: il controllore confronta con CHIAVE_MAGAZZINO? "
        "Alla fine c'è return FORNITORE?")
    assert r.json() == {"fornitore": "Cacao del Loompaland", "magazzino": COME_NUOVO}, \
        'La risposta: {"fornitore": fornitore, "magazzino": MAGAZZINO}'
