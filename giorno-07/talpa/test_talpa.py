"""I test della talpa. NON si modificano: si trova il bug in main.py con il debugger.

    pytest -v
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_bug_1_il_totale():
    risposta = client.get("/bottino/totale")
    assert risposta.status_code == 200
    assert risposta.json() == {"totale": 673000}, "Il totale è sbagliato: quali pezzi sta sommando il for?"


def test_bug_2_la_parte_di_lupin():
    risposta = client.get("/bottino/quota/Lupin")
    assert risposta.status_code == 200
    assert risposta.json() == {"nome": "Lupin", "parte": 201900}, "La parte è sbagliata: guardate tot e parte nel debugger"


def test_bug_3_la_refurtiva_di_una_stanza():
    risposta = client.get("/refurtiva", params={"stanza": "Studio"})
    assert risposta.status_code == 200
    assert [p["id"] for p in risposta.json()] == [2, 3], "Nello studio c'erano due pezzi: guardate risultato a ogni giro"
