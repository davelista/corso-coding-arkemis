"""I test dell'API della flotta. NON si modificano: si modifica main.py finché diventano verdi."""
from itertools import count

import pytest
from fastapi.testclient import TestClient

import main

client = TestClient(main.app)

PERLA = {"nome": "Perla Nera", "capitano": "Jack Sparrow", "bandiera": "pirata", "cannoni": 32, "porto_base": "Tortuga"}
OLANDESE = {"nome": "Olandese Volante", "capitano": "Davy Jones", "bandiera": "pirata", "cannoni": 46, "porto_base": None}
DAUNTLESS = {"nome": "Dauntless", "capitano": "James Norrington", "bandiera": "Marina", "cannoni": 50, "porto_base": "Port Royal"}


@pytest.fixture(autouse=True)
def mare_vuoto():
    """Prima di ogni test la flotta riparte vuota, con gli id da 1."""
    main.flotta.clear()
    main.contatore = count(1)


# ------------------------------------------------ già funzionanti (li abbiamo scritti insieme)
def test_flotta_vuota():
    risposta = client.get("/navi")
    assert risposta.status_code == 200
    assert risposta.json() == []


def test_crea_nave():
    risposta = client.post("/navi", json=PERLA)
    assert risposta.status_code == 201
    assert risposta.json() == {"id": 1, **PERLA}


def test_crea_e_poi_lista():
    client.post("/navi", json=PERLA)
    client.post("/navi", json=OLANDESE)
    nomi = [n["nome"] for n in client.get("/navi").json()]
    assert nomi == ["Perla Nera", "Olandese Volante"]


def test_leggi_nave():
    client.post("/navi", json=PERLA)
    risposta = client.get("/navi/1")
    assert risposta.status_code == 200
    assert risposta.json()["capitano"] == "Jack Sparrow"


def test_leggi_nave_inesistente():
    risposta = client.get("/navi/99")
    assert risposta.status_code == 404
    assert risposta.json() == {"detail": "Nave non trovata"}


def test_nave_senza_porto():
    risposta = client.post("/navi", json=OLANDESE)
    assert risposta.status_code == 201
    assert risposta.json()["porto_base"] is None


# ------------------------------------------------ Pydantic fa la guardia
def test_cannoni_negativi_rifiutati():
    assert client.post("/navi", json={**PERLA, "cannoni": -5}).status_code == 422


def test_bandiera_sconosciuta_rifiutata():
    assert client.post("/navi", json={**PERLA, "bandiera": "unicorni"}).status_code == 422


def test_capitano_mancante_rifiutato():
    senza_capitano = {k: v for k, v in PERLA.items() if k != "capitano"}
    assert client.post("/navi", json=senza_capitano).status_code == 422


# ------------------------------------------------ OBBLIGATORIO: PUT e DELETE
def test_aggiorna_nave():
    client.post("/navi", json=PERLA)
    risposta = client.put("/navi/1", json={**PERLA, "cannoni": 20})
    assert risposta.status_code == 200
    assert risposta.json() == {"id": 1, **PERLA, "cannoni": 20}
    assert client.get("/navi/1").json()["cannoni"] == 20


def test_aggiorna_nave_inesistente():
    risposta = client.put("/navi/99", json=PERLA)
    assert risposta.status_code == 404
    assert risposta.json() == {"detail": "Nave non trovata"}


def test_aggiorna_con_dati_sbagliati():
    client.post("/navi", json=PERLA)
    assert client.put("/navi/1", json={**PERLA, "cannoni": -1}).status_code == 422


def test_affonda_nave():
    client.post("/navi", json=PERLA)
    risposta = client.delete("/navi/1")
    assert risposta.status_code == 204
    assert client.get("/navi/1").status_code == 404


def test_affonda_nave_inesistente():
    risposta = client.delete("/navi/99")
    assert risposta.status_code == 404
    assert risposta.json() == {"detail": "Nave non trovata"}


def test_id_non_riutilizzati():
    client.post("/navi", json=PERLA)
    client.delete("/navi/1")
    risposta = client.post("/navi", json=OLANDESE)
    assert risposta.json()["id"] == 2


# ------------------------------------------------ EXTRA: nomi unici e filtri
def test_nome_duplicato():
    client.post("/navi", json=PERLA)
    risposta = client.post("/navi", json={**OLANDESE, "nome": "Perla Nera"})
    assert risposta.status_code == 409
    assert risposta.json() == {"detail": "Nome già usato"}


def test_aggiorna_tenendo_il_proprio_nome():
    client.post("/navi", json=PERLA)
    assert client.put("/navi/1", json={**PERLA, "capitano": "Hector Barbossa"}).status_code == 200


def test_aggiorna_con_il_nome_di_un_altra():
    client.post("/navi", json=PERLA)
    client.post("/navi", json=OLANDESE)
    risposta = client.put("/navi/2", json={**OLANDESE, "nome": "Perla Nera"})
    assert risposta.status_code == 409
    assert risposta.json() == {"detail": "Nome già usato"}


def test_filtra_per_bandiera():
    client.post("/navi", json=PERLA)
    client.post("/navi", json=DAUNTLESS)
    risposta = client.get("/navi", params={"bandiera": "Marina"})
    assert [n["nome"] for n in risposta.json()] == ["Dauntless"]


def test_filtra_per_cannoni():
    client.post("/navi", json=PERLA)
    client.post("/navi", json=OLANDESE)
    client.post("/navi", json=DAUNTLESS)
    risposta = client.get("/navi", params={"min_cannoni": 40})
    assert [n["nome"] for n in risposta.json()] == ["Olandese Volante", "Dauntless"]


def test_filtri_insieme():
    client.post("/navi", json=PERLA)
    client.post("/navi", json=OLANDESE)
    client.post("/navi", json=DAUNTLESS)
    risposta = client.get("/navi", params={"bandiera": "pirata", "min_cannoni": 40})
    assert [n["nome"] for n in risposta.json()] == ["Olandese Volante"]
