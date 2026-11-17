"""I test della villa su PostgreSQL. NON si modificano.

Lavorano sul database villa_test (va creato una volta sola: createdb villa_test).
Prima di ogni test, villa_test viene rifatto da capo con villa.sql:
i vostri dati nel database villa non vengono toccati.

    pytest -v -k livello_1
"""
import os
from pathlib import Path

os.environ["VILLA_DB"] = "villa_test"   # prima di importare main: i test non toccano il database villa

import psycopg
import pytest
from fastapi.testclient import TestClient
from psycopg.rows import dict_row

from main import app

client = TestClient(app)
SCHEMA = (Path(__file__).parent / "villa.sql").read_text()


def sql(query, valori=None):
    """Chiede direttamente al database villa_test, senza passare dall'API."""
    with psycopg.connect(dbname="villa_test", row_factory=dict_row) as conn:
        return conn.execute(query, valori).fetchall()


@pytest.fixture(autouse=True)
def villa_come_nuova():
    with psycopg.connect(dbname="villa_test") as conn:
        conn.execute(SCHEMA)


SERNINE = {"nome": "Paul Sernine", "professione": "collezionista"}
KARIM = {"nome": "Karim Haddad", "stanza_id": 9, "turno": "notte", "anni_servizio": 20}


# ------------------------------------------------------------ l'esempio (già verde)
def test_esempio_lista_dal_database():
    risposta = client.get("/ospiti")
    assert risposta.status_code == 200
    assert len(risposta.json()) == 8


# ------------------------------------------------------------ livello 1
def test_livello_1_un_ospite():
    risposta = client.get("/ospiti/4")
    assert risposta.status_code == 200
    assert risposta.json() == {"id": 4, "nome": "Isabelle Moreau", "professione": "gallerista"}


def test_livello_1_ospite_che_non_esiste():
    risposta = client.get("/ospiti/99")
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Ospite non trovato"


# ------------------------------------------------------------ livello 2
def test_livello_2_nuovo_ospite():
    risposta = client.post("/ospiti", json=SERNINE)
    assert risposta.status_code == 201, "Una POST che crea risponde 201: status_code nel decoratore"
    assert risposta.json() == {"id": 9, **SERNINE}


def test_livello_2_l_ospite_e_nel_database():
    client.post("/ospiti", json=SERNINE)
    righe = sql("SELECT * FROM ospiti WHERE nome = %s", ("Paul Sernine",))
    assert len(righe) == 1, "L'ospite non è nel database: c'è l'INSERT? Il with si è chiuso senza errori?"


# ------------------------------------------------------------ livello 3
def test_livello_3_cancella_un_ospite():
    risposta = client.delete("/ospiti/8")
    assert risposta.status_code == 204, "Manca la rotta DELETE /ospiti/{ospite_id}, o il 204"
    assert sql("SELECT * FROM ospiti WHERE id = 8") == []


def test_livello_3_ospite_che_non_esiste():
    risposta = client.delete("/ospiti/99")
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Ospite non trovato"


# ------------------------------------------------------------ livello 4
def test_livello_4_sposta_una_guardia():
    risposta = client.put("/guardie/3", json=KARIM)
    assert risposta.status_code == 200, "Manca la rotta PUT /guardie/{guardia_id}"
    assert risposta.json() == {"id": 3, **KARIM}
    assert sql("SELECT stanza_id FROM guardie WHERE id = 3") == [{"stanza_id": 9}]


def test_livello_4_guardia_che_non_esiste():
    risposta = client.put("/guardie/42", json=KARIM)
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Guardia non trovata"


# ------------------------------------------------------------ extra
def test_extra_le_guardie_di_una_stanza():
    risposta = client.get("/stanze/1/guardie")
    assert risposta.status_code == 200
    assert sorted(g["id"] for g in risposta.json()) == [1, 8]
    assert client.get("/stanze/42/guardie").status_code == 404


def test_extra_nome_gia_in_lista():
    risposta = client.post("/ospiti", json={"nome": "Isabelle Moreau", "professione": "gallerista"})
    assert risposta.status_code == 409
    assert risposta.json()["detail"] == "Nome già in lista"


def test_extra_stanza_che_non_esiste():
    risposta = client.put("/guardie/3", json={**KARIM, "stanza_id": 42})
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Stanza non trovata"
