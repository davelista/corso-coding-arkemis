"""I test del colpo. NON si modificano: si modifica main.py finché diventano verdi.

Un livello alla volta:   pytest -v -k livello_1
Tutto insieme:           pytest -v
"""
import pytest
from fastapi.testclient import TestClient

import villa
from main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def villa_come_nuova():
    """Prima di ogni test, la villa torna com'era all'inizio della serata."""
    villa.ricarica()


def ids(lista):
    return sorted(elemento["id"] for elemento in lista)


# ------------------------------------------------------------ esempi (già verdi)
def test_esempio_lista_ospiti():
    risposta = client.get("/ospiti")
    assert risposta.status_code == 200
    assert len(risposta.json()) == 8


def test_esempio_ospite_che_non_esiste():
    risposta = client.get("/ospiti/99")
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Ospite non trovato"


# ------------------------------------------------------------ livello 1
def test_livello_1_la_lista_risponde():
    risposta = client.get("/stanze")
    assert risposta.status_code == 200
    assert risposta.json() != [], "La lista è vuota: le stanze non segrete vanno aggiunte a visibili"


def test_livello_1_niente_stanze_segrete():
    stanze = client.get("/stanze").json()
    nomi = [s["nome"] for s in stanze]
    assert "Caveau" not in nomi, "Il caveau è segreto: non deve comparire nella lista"
    assert "Biblioteca" in nomi
    assert all(s["segreta"] is False for s in stanze)


# ------------------------------------------------------------ livello 2
def test_livello_2_una_stanza():
    risposta = client.get("/stanze/4")
    assert risposta.status_code == 200
    assert risposta.json()["nome"] == "Biblioteca"


def test_livello_2_anche_le_segrete_con_l_id():
    risposta = client.get("/stanze/10")
    assert risposta.status_code == 200, "Con l'id, la stanza si legge anche se è segreta"
    assert risposta.json()["segreta"] is True


def test_livello_2_stanza_che_non_esiste():
    risposta = client.get("/stanze/42")
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Stanza non trovata"


# ------------------------------------------------------------ livello 3
def test_livello_3_tutte_le_telecamere():
    risposta = client.get("/telecamere")
    assert risposta.status_code == 200, "Manca la rotta GET /telecamere"
    assert len(risposta.json()) == 14


def test_livello_3_filtro_per_stanza():
    risposta = client.get("/telecamere", params={"stanza_id": 6})
    assert risposta.status_code == 200
    assert ids(risposta.json()) == [5, 6]


def test_livello_3_stanza_senza_telecamere():
    risposta = client.get("/telecamere", params={"stanza_id": 9})
    assert risposta.status_code == 200
    assert risposta.json() == [], "Nessuna telecamera in cantina: la risposta è una lista vuota, non un 404"


# ------------------------------------------------------------ livello 4
def test_livello_4_le_guardie_di_una_stanza():
    risposta = client.get("/stanze/1/guardie")
    assert risposta.status_code == 200, "Manca la rotta GET /stanze/{stanza_id}/guardie"
    assert ids(risposta.json()) == [1, 8]


def test_livello_4_stanza_senza_guardie():
    risposta = client.get("/stanze/4/guardie")
    assert risposta.status_code == 200
    assert risposta.json() == []


def test_livello_4_stanza_che_non_esiste():
    risposta = client.get("/stanze/42/guardie")
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Stanza non trovata"


# ------------------------------------------------------------ livello 5
def test_livello_5_nuovo_ospite():
    risposta = client.post("/ospiti", json={"nome": "Lucie Cassin", "professione": "pianista"})
    assert risposta.status_code == 201, "Una POST che crea risponde 201: status_code nel decoratore"
    assert risposta.json() == {"id": 9, "nome": "Lucie Cassin", "professione": "pianista"}


def test_livello_5_l_ospite_resta_in_lista():
    client.post("/ospiti", json={"nome": "Lucie Cassin", "professione": "pianista"})
    risposta = client.get("/ospiti/9")
    assert risposta.status_code == 200, "Il nuovo ospite va messo nel dizionario ospiti"
    assert risposta.json()["nome"] == "Lucie Cassin"


def test_livello_5_dati_mancanti():
    risposta = client.post("/ospiti", json={"nome": "Lucie Cassin"})
    assert risposta.status_code == 422, "Manca la professione: Pydantic deve rifiutare (il corpo è un OspiteNuovo?)"


# ------------------------------------------------------------ livello 6
NUOVA_CLAIRE = {"nome": "Claire Dubois", "stanza_id": 7, "turno": "notte", "anni_servizio": 4}


def test_livello_6_sostituisce_la_guardia():
    risposta = client.put("/guardie/2", json=NUOVA_CLAIRE)
    assert risposta.status_code == 200, "Manca la rotta PUT /guardie/{guardia_id}"
    assert risposta.json() == {"id": 2, **NUOVA_CLAIRE}


def test_livello_6_la_modifica_resta():
    client.put("/guardie/2", json=NUOVA_CLAIRE)
    assert villa.guardie[2].stanza_id == 7, "La guardia nuova va rimessa nel dizionario guardie, con lo stesso id"
    assert villa.guardie[2].id == 2, "Nel dizionario va una Guardia (con l'id), non una GuardiaNuova"


def test_livello_6_guardia_che_non_esiste():
    risposta = client.put("/guardie/42", json=NUOVA_CLAIRE)
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Guardia non trovata"


# ------------------------------------------------------------ livello 7
def test_livello_7_spegne_la_telecamera():
    risposta = client.delete("/telecamere/1")
    assert risposta.status_code == 204, "Manca la rotta DELETE /telecamere/{telecamera_id}, o il 204"
    assert risposta.content == b""


def test_livello_7_la_telecamera_sparisce():
    client.delete("/telecamere/1")
    assert 1 not in villa.telecamere, "La telecamera va tolta dal dizionario: del telecamere[...]"


def test_livello_7_telecamera_che_non_esiste():
    client.delete("/telecamere/1")
    risposta = client.delete("/telecamere/1")
    assert risposta.status_code == 404, "La seconda volta la telecamera non c'è più: 404"
    assert risposta.json()["detail"] == "Telecamera non trovata"


# ------------------------------------------------------------ finale
def test_finale_senza_piano_la_cassaforte_resta_chiusa():
    risposta = client.post("/cassaforte/apri", json={"combinazione": "0000"})
    assert risposta.status_code == 403


def test_finale_il_piano_funziona_fino_alla_combinazione():
    # Il piano, tutto via API: niente scorciatoie sul dizionario.
    client.post("/ospiti", json={"nome": "Paul Sernine", "professione": "collezionista"})
    for guardia in client.get("/stanze/3/guardie").json():
        client.put(f"/guardie/{guardia['id']}", json={**{k: guardia[k] for k in ("nome", "turno", "anni_servizio")}, "stanza_id": 9})
    for telecamera in client.get("/telecamere", params={"stanza_id": 3}).json():
        client.delete(f"/telecamere/{telecamera['id']}")
    risposta = client.post("/cassaforte/apri", json={"combinazione": "0000"})
    assert risposta.status_code == 403
    assert "combinazione" in risposta.json()["detail"], f"Il piano non è completo: {risposta.json()['detail']}"


# ------------------------------------------------------------ extra
def test_extra_nome_gia_in_lista():
    risposta = client.post("/ospiti", json={"nome": "Isabelle Moreau", "professione": "gallerista"})
    assert risposta.status_code == 409
    assert risposta.json()["detail"] == "Nome già in lista"


def test_extra_solo_le_telecamere_accese():
    risposta = client.get("/telecamere", params={"stanza_id": 6, "accesa": True})
    assert risposta.status_code == 200
    assert ids(risposta.json()) == [5]


def test_extra_guardie_per_turno():
    risposta = client.get("/guardie", params={"turno": "sera"})
    assert risposta.status_code == 200
    assert ids(risposta.json()) == [1, 2, 6, 9]


# ------------------------------------------------------------ bonus · PATCH
def test_bonus_patch_cambia_solo_un_campo():
    risposta = client.patch("/guardie/3", json={"stanza_id": 8})
    assert risposta.status_code == 200
    assert risposta.json() == {"id": 3, "nome": "Karim Haddad", "stanza_id": 8, "turno": "notte", "anni_servizio": 20}


def test_bonus_patch_guardia_che_non_esiste():
    assert client.patch("/guardie/3", json={"turno": "sera"}).status_code == 200, "Manca la rotta PATCH /guardie/{guardia_id}"
    risposta = client.patch("/guardie/42", json={"stanza_id": 8})
    assert risposta.status_code == 404
