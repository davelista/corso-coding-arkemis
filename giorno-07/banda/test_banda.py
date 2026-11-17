"""I test della banda. NON si modificano: si modifica main.py finché diventano verdi.

    pytest -v -k post       solo la POST
    pytest -v -k put        solo la PUT
    pytest -v -k delete     solo la DELETE
"""
import pytest
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)

GUERCHARD = {"nome": "Guerchard", "specialita": "travestimenti", "quota": 10}


@pytest.fixture(autouse=True)
def banda_come_nuova():
    main.ricarica()


# ------------------------------------------------------------ esempi (già verdi)
def test_esempio_lista():
    assert len(client.get("/complici").json()) == 3


def test_esempio_complice_che_non_esiste():
    assert client.get("/complici/9").status_code == 404


# ------------------------------------------------------------ POST
def test_post_nuovo_complice():
    risposta = client.post("/complici", json=GUERCHARD)
    assert risposta.status_code == 201, "Manca la rotta POST /complici, o lo status_code 201"
    assert risposta.json() == {"id": 4, **GUERCHARD}


def test_post_il_complice_resta():
    client.post("/complici", json=GUERCHARD)
    assert client.get("/complici/4").status_code == 200, "Il nuovo complice va messo nel dizionario banda"


def test_post_quota_sbagliata():
    risposta = client.post("/complici", json={**GUERCHARD, "quota": 150})
    assert risposta.status_code == 422, "Il corpo deve essere un CompliceNuovo: Pydantic rifiuta quota 150"


# ------------------------------------------------------------ PUT
def test_put_cambia_la_quota():
    risposta = client.put("/complici/3", json={"nome": "Le Ballu", "specialita": "fuga", "quota": 30})
    assert risposta.status_code == 200, "Manca la rotta PUT /complici/{complice_id}"
    assert risposta.json() == {"id": 3, "nome": "Le Ballu", "specialita": "fuga", "quota": 30}
    assert client.get("/complici/3").json()["quota"] == 30, "Il complice nuovo va rimesso nel dizionario"


def test_put_complice_che_non_esiste():
    risposta = client.put("/complici/9", json=GUERCHARD)
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Complice non trovato"


# ------------------------------------------------------------ DELETE
def test_delete_lascia_la_banda():
    risposta = client.delete("/complici/2")
    assert risposta.status_code == 204, "Manca la rotta DELETE /complici/{complice_id}, o lo status_code 204"
    assert client.get("/complici/2").status_code == 404, "Il complice va tolto dal dizionario: del banda[...]"


def test_delete_complice_che_non_esiste():
    risposta = client.delete("/complici/9")
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Complice non trovato"


# ------------------------------------------------------------ extra
def test_extra_nome_gia_nella_banda():
    risposta = client.post("/complici", json={**GUERCHARD, "nome": "Grognard"})
    assert risposta.status_code == 409
    assert risposta.json()["detail"] == "Nome già nella banda"


def test_extra_filtro_per_specialita():
    risposta = client.get("/complici", params={"specialita": "fuga"})
    assert [c["id"] for c in risposta.json()] == [3]
