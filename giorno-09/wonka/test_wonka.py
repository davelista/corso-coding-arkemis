"""I test della fabbrica. NON si modificano.

Lavorano sul database wonka_test (va creato una volta sola: createdb wonka_test).
Prima di ogni test, wonka_test viene rifatto da capo con wonka.sql.
Ogni livello si prova da solo: i bambini dei test li mettiamo noi nel database.

    pytest -v -k livello_1
"""
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

os.environ["WONKA_DB"] = "wonka_test"                  # i test non toccano il database wonka
os.environ["SECRET_KEY"] = "chiave-solo-per-i-test-della-fabbrica-wonka"    # e non leggono la vostra chiave

import jwt
import psycopg
import pytest
from fastapi.testclient import TestClient
from psycopg.rows import dict_row

from main import app
from sicurezza import calcola_hash, crea_biglietto

client = TestClient(app)
SCHEMA = (Path(__file__).parent / "wonka.sql").read_text()

CHARLIE = {"username": "charlie", "nome": "Charlie Bucket", "password": "cioccolato"}


def sql(query, valori=None):
    """Chiede direttamente al database wonka_test, senza passare dall'API."""
    with psycopg.connect(dbname="wonka_test", row_factory=dict_row) as conn:
        return conn.execute(query, valori).fetchall()


@pytest.fixture(autouse=True)
def fabbrica_come_nuova():
    with psycopg.connect(dbname="wonka_test") as conn:
        conn.execute(SCHEMA)


def charlie_nel_database() -> int:
    """Mette Charlie nel database (con l'impronta, come la registrazione) e restituisce il suo id."""
    righe = sql("INSERT INTO bambini (username, nome, password_hash) VALUES (%s, %s, %s) RETURNING id",
                (CHARLIE["username"], CHARLIE["nome"], calcola_hash(CHARLIE["password"])))
    return righe[0]["id"]


def con_biglietto(bambino_id: int) -> dict:
    """L'header che manderebbe Postman: Authorization: Bearer <biglietto>."""
    return {"Authorization": f"Bearer {crea_biglietto(bambino_id)}"}


# ------------------------------------------------------------ l'esempio (già verde)
def test_esempio_la_vetrina():
    risposta = client.get("/sale")
    assert risposta.status_code == 200
    assert len(risposta.json()) == 5
    assert "ingrediente" not in risposta.json()[0], "Nella vetrina gli ingredienti non si vedono"


# ------------------------------------------------------------ livello 1
def test_livello_1_registrazione():
    risposta = client.post("/bambini", json=CHARLIE)
    assert risposta.status_code == 201, "Manca la rotta POST /bambini, o il 201 nel decoratore"
    assert risposta.json() == {"id": 1, "username": "charlie", "nome": "Charlie Bucket"}, \
        "La risposta è un Bambino: id, username, nome. Mai la password, mai l'impronta"


def test_livello_1_nel_database_c_e_solo_l_impronta():
    client.post("/bambini", json=CHARLIE)
    righe = sql("SELECT * FROM bambini WHERE username = 'charlie'")
    assert len(righe) == 1, "Charlie non è nel database: c'è il db.commit()?"
    assert righe[0]["password_hash"] != "cioccolato", "Nel database c'è la password in chiaro: usate calcola_hash"
    assert righe[0]["password_hash"].startswith("$argon2"), "password_hash deve essere calcola_hash(dati.password)"


def test_livello_1_password_troppo_corta():
    risposta = client.post("/bambini", json={**CHARLIE, "password": "corta"})
    assert risposta.status_code == 422, "Il corpo deve essere un BambinoNuovo: Pydantic controlla gli 8 caratteri"


# ------------------------------------------------------------ livello 2
def test_livello_2_login_giusto():
    charlie_id = charlie_nel_database()
    risposta = client.post("/login", json={"username": "charlie", "password": "cioccolato"})
    assert risposta.status_code == 200, "Manca la rotta POST /login?"
    biglietto = risposta.json()
    assert biglietto["token_type"] == "bearer"
    dentro = jwt.decode(biglietto["access_token"], "chiave-solo-per-i-test-della-fabbrica-wonka", algorithms=["HS256"])
    assert dentro["sub"] == str(charlie_id), "Il biglietto si crea con crea_biglietto(bambino.id)"


def test_livello_2_password_sbagliata():
    charlie_nel_database()
    risposta = client.post("/login", json={"username": "charlie", "password": "caramella"})
    assert risposta.status_code == 401
    assert risposta.json()["detail"] == "Username o password sbagliati"


def test_livello_2_username_che_non_esiste():
    risposta = client.post("/login", json={"username": "augustus", "password": "cioccolato"})
    assert risposta.status_code == 401, "Nessun bambino con quell'username: stesso 401 della password sbagliata"
    assert risposta.json()["detail"] == "Username o password sbagliati"


# ------------------------------------------------------------ livello 3
def test_livello_3_chi_sono():
    charlie_id = charlie_nel_database()
    risposta = client.get("/me", headers=con_biglietto(charlie_id))
    assert risposta.status_code == 200, "Manca la rotta GET /me"
    assert risposta.json() == {"id": charlie_id, "username": "charlie", "nome": "Charlie Bucket"}


def test_livello_3_senza_biglietto():
    risposta = client.get("/me")
    assert risposta.status_code == 401, "Senza biglietto: 401. Nel def manca Depends(bambino_corrente)?"


def test_livello_3_biglietto_falso():
    risposta = client.get("/me", headers={"Authorization": "Bearer biglietto-disegnato-a-mano"})
    assert risposta.status_code == 401


# ------------------------------------------------------------ livello 4
def test_livello_4_entro_nella_sala():
    charlie_id = charlie_nel_database()
    risposta = client.get("/sale/3", headers=con_biglietto(charlie_id))
    assert risposta.status_code == 200, "Manca la rotta GET /sale/{sala_id}"
    assert risposta.json()["nome"] == "Sala del cioccolato"
    assert risposta.json()["ingrediente"] == "Latte del fiume di cioccolato", "La risposta è una Sala, con l'ingrediente"


def test_livello_4_senza_biglietto():
    risposta = client.get("/sale/3")
    assert risposta.status_code == 401, "Le sale si vedono solo con il biglietto: Depends(bambino_corrente)"


def test_livello_4_sala_che_non_esiste():
    charlie_id = charlie_nel_database()
    risposta = client.get("/sale/42", headers=con_biglietto(charlie_id))
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Sala non trovata"


# ------------------------------------------------------------ il finale
def test_finale_la_ricetta():
    charlie_id = charlie_nel_database()
    assert client.post("/ricetta", json={"parola": "CACAO"}, headers=con_biglietto(charlie_id)).status_code == 400
    assert client.post("/ricetta", json={"parola": "?"}).status_code == 401


# ------------------------------------------------------------ extra
def test_extra_username_gia_preso():
    client.post("/bambini", json=CHARLIE)
    risposta = client.post("/bambini", json={**CHARLIE, "nome": "Un altro Charlie"})
    assert risposta.status_code == 409
    assert risposta.json()["detail"] == "Username già preso"


def test_extra_cambio_il_mio_nome():
    charlie_id = charlie_nel_database()
    risposta = client.put("/me", json={"nome": "Charlie B."}, headers=con_biglietto(charlie_id))
    assert risposta.status_code == 200
    assert risposta.json()["nome"] == "Charlie B."
    assert sql("SELECT nome FROM bambini WHERE id = %s", (charlie_id,)) == [{"nome": "Charlie B."}]


def test_extra_biglietto_scaduto():
    charlie_id = charlie_nel_database()
    ieri = datetime.now(timezone.utc) - timedelta(days=1)
    scaduto = jwt.encode({"sub": str(charlie_id), "exp": ieri}, "chiave-solo-per-i-test-della-fabbrica-wonka", algorithm="HS256")
    risposta = client.get("/me", headers={"Authorization": f"Bearer {scaduto}"})
    assert risposta.status_code == 401, "Questo è già verde se il livello 3 funziona: il controllore guarda exp"
