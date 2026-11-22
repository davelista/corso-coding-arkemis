"""I test di Agrabah. NON si modificano.

Lavorano sul database agrabah_test (va creato una volta sola: createdb agrabah_test).
Prima di ogni test, agrabah_test viene rifatto da capo con agrabah.sql: sei tesori, nessun padrone.
Ogni livello si prova da solo:

    pytest -v -k livello_1

Se un test è rosso, leggete l'ultima riga del messaggio: è scritta per voi.
"""
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

os.environ["AGRABAH_DB"] = "agrabah_test"                      # i test non toccano il database agrabah
os.environ["CHIAVE_CAVERNA"] = "apriti-sesamo-solo-per-i-test"  # e non leggono le vostre chiavi
os.environ["SECRET_KEY"] = "chiave-solo-per-i-test-della-lampada-di-agrabah"

import jwt
import psycopg
import pytest
from fastapi.testclient import TestClient
from psycopg.rows import dict_row

from main import app

client = TestClient(app)
SCHEMA = (Path(__file__).parent / "agrabah.sql").read_text()

CHIAVE = {"X-API-Key": "apriti-sesamo-solo-per-i-test"}
ANELLO = {"nome": "Anello del sultano", "valore": 300}
ALADDIN = {"username": "aladdin", "nome": "Aladdin", "password": "tappeto-volante"}


def sql(query, valori=None):
    """Chiede direttamente al database agrabah_test, senza passare dall'API."""
    with psycopg.connect(dbname="agrabah_test", row_factory=dict_row) as conn:
        cur = conn.execute(query, valori)
        return cur.fetchall() if cur.description else []


@pytest.fixture(autouse=True)
def agrabah_come_nuova():
    with psycopg.connect(dbname="agrabah_test") as conn:
        conn.execute(SCHEMA)


def padrone_nel_database(username="aladdin", nome="Aladdin", password="tappeto-volante", ruolo="padrone") -> int:
    """Mette un padrone nel database (con l'impronta, come la registrazione) e restituisce il suo id."""
    from sicurezza import calcola_hash          # serve dal livello 3: è in sicurezza.py?
    righe = sql("INSERT INTO padroni (username, nome, password_hash, ruolo) VALUES (%s, %s, %s, %s) RETURNING id",
                (username, nome, calcola_hash(password), ruolo))
    return righe[0]["id"]


def con_token(padrone_id: int) -> dict:
    """L'header che manderebbe Postman: Authorization: Bearer <token>."""
    from sicurezza import crea_token            # serve dal livello 4: è in sicurezza.py?
    return {"Authorization": f"Bearer {crea_token(padrone_id)}"}


def desiderio_nel_database(testo: str, padrone_id: int) -> int:
    return sql("INSERT INTO desideri (testo, padrone_id) VALUES (%s, %s) RETURNING id", (testo, padrone_id))[0]["id"]


# ------------------------------------------------------------ livello 0 · arrivo ad Agrabah
def test_livello_0_la_citta():
    risposta = client.get("/")
    assert risposta.status_code == 200, "Manca la rotta GET /"
    assert risposta.json() == {"citta": "Agrabah"}, 'GET / risponde con {"citta": "Agrabah"}'


# ------------------------------------------------------------ livello 1 · il bazar
def test_livello_1_tutti_i_tesori():
    risposta = client.get("/tesori")
    assert risposta.status_code == 200, "Manca la rotta GET /tesori"
    tesori = risposta.json()
    assert len(tesori) == 6, "Nel bazar ci sono sei tesori"
    assert tesori[0] == {"id": 1, "nome": "Lampada a olio", "valore": 3, "maledetto": False}, \
        "Ogni tesoro ha id, nome, valore, maledetto: è lo stampo Tesoro"
    assert [t["id"] for t in tesori] == [1, 2, 3, 4, 5, 6], "I tesori vanno in ordine di id: order_by"


def test_livello_1_filtro_valore_min():
    risposta = client.get("/tesori", params={"valore_min": 500})
    assert risposta.status_code == 200
    assert [t["nome"] for t in risposta.json()] == ["Tappeto volante", "Rubino della scimmia", "Clessidra rossa"], \
        "?valore_min=500: solo i tesori che valgono 500 o più"


def test_livello_1_filtro_maledetto():
    maledetti = client.get("/tesori", params={"maledetto": "true"}).json()
    sicuri = client.get("/tesori", params={"maledetto": "false"}).json()
    assert [t["nome"] for t in maledetti] == ["Rubino della scimmia", "Clessidra rossa"], "?maledetto=true: solo i maledetti"
    assert len(sicuri) == 4, "?maledetto=false: solo i quattro sicuri. Attenti: False non è «il filtro non c'è»"


def test_livello_1_due_filtri_insieme():
    risposta = client.get("/tesori", params={"valore_min": 500, "maledetto": "false"})
    assert [t["nome"] for t in risposta.json()] == ["Tappeto volante"], "I due filtri valgono insieme"


def test_livello_1_un_tesoro():
    risposta = client.get("/tesori/2")
    assert risposta.status_code == 200, "Manca la rotta GET /tesori/{tesoro_id}"
    assert risposta.json() == {"id": 2, "nome": "Tappeto volante", "valore": 800, "maledetto": False}


def test_livello_1_un_tesoro_che_non_esiste():
    risposta = client.get("/tesori/999")
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Tesoro non trovato"


def test_livello_1_nuovo_tesoro():
    risposta = client.post("/tesori", json=ANELLO, headers=CHIAVE)
    assert risposta.status_code == 201, "Manca la rotta POST /tesori, o il 201 nel decoratore"
    assert risposta.json() == {"id": 7, "nome": "Anello del sultano", "valore": 300, "maledetto": False}, \
        "La risposta è il Tesoro con il suo id. Se maledetto manca nel corpo, vale False"
    assert sql("SELECT nome FROM tesori WHERE id = 7") == [{"nome": "Anello del sultano"}], \
        "Il tesoro non è nel database: c'è il db.commit()?"


def test_livello_1_nuovo_tesoro_sbagliato():
    assert client.post("/tesori", json={"nome": "", "valore": 10}, headers=CHIAVE).status_code == 422, \
        "Il nome non può essere vuoto: Field(min_length=1) nello stampo TesoroNuovo"
    assert client.post("/tesori", json={"nome": "Sabbia", "valore": -5}, headers=CHIAVE).status_code == 422, \
        "Il valore non può essere negativo: Field(ge=0) nello stampo TesoroNuovo"


def test_livello_1_cambio_un_tesoro():
    nuovo = {"nome": "Tappeto volante, rammendato", "valore": 650, "maledetto": True}
    risposta = client.put("/tesori/2", json=nuovo, headers=CHIAVE)
    assert risposta.status_code == 200, "Manca la rotta PUT /tesori/{tesoro_id}"
    assert risposta.json() == {"id": 2, **nuovo}
    assert sql("SELECT nome, valore, maledetto FROM tesori WHERE id = 2") == [nuovo], \
        "Il tesoro nel database non è cambiato: c'è il db.commit()?"
    assert len(sql("SELECT id FROM tesori")) == 6, "La PUT cambia un tesoro che c'è: non ne aggiunge un altro"


def test_livello_1_cambio_un_tesoro_che_non_esiste():
    risposta = client.put("/tesori/999", json=ANELLO, headers=CHIAVE)
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Tesoro non trovato"


def test_livello_1_tolgo_un_tesoro():
    risposta = client.delete("/tesori/6", headers=CHIAVE)
    assert risposta.status_code == 204, "Manca la rotta DELETE /tesori/{tesoro_id}, o il 204 nel decoratore"
    assert risposta.content == b"", "Il 204 non ha corpo: la rotta non restituisce niente"
    assert sql("SELECT id FROM tesori WHERE id = 6") == [], "Il tesoro è ancora nel database: db.delete e db.commit"


def test_livello_1_tolgo_un_tesoro_che_non_esiste():
    risposta = client.delete("/tesori/999", headers=CHIAVE)
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Tesoro non trovato"


# ------------------------------------------------------------ livello 2 · la Caverna
def test_livello_2_senza_chiave():
    for risposta in (client.post("/tesori", json=ANELLO),
                     client.put("/tesori/2", json=ANELLO),
                     client.delete("/tesori/6")):
        assert risposta.status_code == 401, "Senza header X-API-Key, POST, PUT e DELETE rispondono 401"
        assert risposta.json()["detail"] == "Manca la chiave"
    assert len(sql("SELECT id FROM tesori")) == 6, "Senza chiave non deve cambiare niente nel database"


def test_livello_2_chiave_sbagliata():
    sbagliata = {"X-API-Key": "apriti-cetriolo"}
    for risposta in (client.post("/tesori", json=ANELLO, headers=sbagliata),
                     client.put("/tesori/2", json=ANELLO, headers=sbagliata),
                     client.delete("/tesori/6", headers=sbagliata)):
        assert risposta.status_code == 401
        assert risposta.json()["detail"] == "Chiave sbagliata"


def test_livello_2_con_la_chiave():
    assert client.post("/tesori", json=ANELLO, headers=CHIAVE).status_code == 201, \
        "Con la chiave giusta si entra. La chiave si legge da os.environ, dopo load_dotenv: non va scritta nel codice"
    assert client.put("/tesori/2", json=ANELLO, headers=CHIAVE).status_code == 200
    assert client.delete("/tesori/6", headers=CHIAVE).status_code == 204


def test_livello_2_guardare_resta_libero():
    assert client.get("/tesori").status_code == 200, "Le due GET restano aperte a tutti: niente Depends"
    assert client.get("/tesori/1").status_code == 200


def test_livello_2_prima_la_chiave_poi_il_404():
    risposta = client.put("/tesori/999", json=ANELLO)
    assert risposta.status_code == 401, "Senza chiave non si arriva nemmeno a cercare il tesoro: 401, non 404"


# ------------------------------------------------------------ livello 3 · chi sei?
def test_livello_3_registrazione():
    risposta = client.post("/padroni", json=ALADDIN)
    assert risposta.status_code == 201, "Manca la rotta POST /padroni, o il 201 nel decoratore"
    assert risposta.json() == {"id": 1, "username": "aladdin", "nome": "Aladdin"}, \
        "La risposta è un Padrone: id, username, nome. Mai la password, mai l'impronta"


def test_livello_3_nel_database_c_e_solo_l_impronta():
    client.post("/padroni", json=ALADDIN)
    righe = sql("SELECT * FROM padroni WHERE username = 'aladdin'")
    assert len(righe) == 1, "Aladdin non è nel database: c'è il db.commit()?"
    assert righe[0]["password_hash"] != "tappeto-volante", "Nel database c'è la password in chiaro: usate calcola_hash"
    assert righe[0]["password_hash"].startswith("$argon2"), "password_hash deve essere calcola_hash(dati.password), con pwdlib"
    assert righe[0]["ruolo"] == "padrone", "Chi si registra è un padrone, non un genio"


def test_livello_3_username_gia_preso():
    client.post("/padroni", json=ALADDIN)
    risposta = client.post("/padroni", json={**ALADDIN, "nome": "Un altro Aladdin"})
    assert risposta.status_code == 409, "Username doppio: il database dice di no (IntegrityError). Rollback, poi 409"
    assert risposta.json()["detail"] == "Username già preso"


def test_livello_3_dati_sbagliati():
    assert client.post("/padroni", json={**ALADDIN, "password": "corta"}).status_code == 422, \
        "La password ha almeno 8 caratteri: Field(min_length=8)"
    assert client.post("/padroni", json={**ALADDIN, "username": "al"}).status_code == 422, \
        "Lo username ha da 3 a 30 caratteri: Field(min_length=3, max_length=30)"
    assert client.post("/padroni", json={**ALADDIN, "nome": ""}).status_code == 422, "Il nome non può essere vuoto"


# ------------------------------------------------------------ livello 4 · la lampada
def test_livello_4_login_giusto():
    aladdin_id = padrone_nel_database()
    risposta = client.post("/login", json={"username": "aladdin", "password": "tappeto-volante"})
    assert risposta.status_code == 200, "Manca la rotta POST /login?"
    token = risposta.json()
    assert token["token_type"] == "bearer"
    dentro = jwt.decode(token["access_token"], "chiave-solo-per-i-test-della-lampada-di-agrabah", algorithms=["HS256"])
    assert dentro["sub"] == str(aladdin_id), 'Nel token, "sub" è l\'id del padrone, scritto come testo: str(padrone.id)'
    assert "exp" in dentro, 'Nel token manca "exp", la scadenza'


def test_livello_4_password_sbagliata():
    padrone_nel_database()
    risposta = client.post("/login", json={"username": "aladdin", "password": "tappeto-persiano"})
    assert risposta.status_code == 401
    assert risposta.json()["detail"] == "Username o password sbagliati"


def test_livello_4_username_che_non_esiste():
    risposta = client.post("/login", json={"username": "jafar", "password": "tappeto-volante"})
    assert risposta.status_code == 401, "Nessun padrone con quello username: stesso 401 della password sbagliata"
    assert risposta.json()["detail"] == "Username o password sbagliati"


def test_livello_4_chi_sono():
    aladdin_id = padrone_nel_database()
    risposta = client.get("/me", headers=con_token(aladdin_id))
    assert risposta.status_code == 200, "Manca la rotta GET /me"
    assert risposta.json() == {"id": aladdin_id, "username": "aladdin", "nome": "Aladdin"}


def test_livello_4_senza_token():
    risposta = client.get("/me")
    assert risposta.status_code == 401, "Senza token: 401. Nel def manca Depends(padrone_corrente)?"
    assert risposta.json()["detail"] == "Manca il token"


def test_livello_4_token_falso():
    risposta = client.get("/me", headers={"Authorization": "Bearer token-disegnato-a-mano"})
    assert risposta.status_code == 401
    assert risposta.json()["detail"] == "Token non valido"


def test_livello_4_token_scaduto():
    aladdin_id = padrone_nel_database()
    ieri = datetime.now(timezone.utc) - timedelta(days=1)
    scaduto = jwt.encode({"sub": str(aladdin_id), "exp": ieri}, "chiave-solo-per-i-test-della-lampada-di-agrabah", algorithm="HS256")
    risposta = client.get("/me", headers={"Authorization": f"Bearer {scaduto}"})
    assert risposta.status_code == 401, "Il token scaduto non vale: jwt.decode guarda exp, e solleva InvalidTokenError"
    assert risposta.json()["detail"] == "Token non valido"


# ------------------------------------------------------------ livello 5 · tre desideri
def test_livello_5_esprimo_un_desiderio():
    aladdin_id = padrone_nel_database()
    risposta = client.post("/desideri", json={"testo": "Un palazzo per Jasmine"}, headers=con_token(aladdin_id))
    assert risposta.status_code == 201, "Manca la rotta POST /desideri, o il 201 nel decoratore"
    assert risposta.json() == {"id": 1, "testo": "Un palazzo per Jasmine", "esaudito": False}, \
        "La risposta è un Desiderio: id, testo, esaudito"
    assert sql("SELECT padrone_id FROM desideri WHERE id = 1") == [{"padrone_id": aladdin_id}], \
        "Il desiderio è del padrone del token: padrone_id=padrone.id"


def test_livello_5_il_quarto_desiderio():
    aladdin_id = padrone_nel_database()
    token = con_token(aladdin_id)
    for testo in ("Un palazzo", "Un elefante", "Una scimmia"):
        assert client.post("/desideri", json={"testo": testo}, headers=token).status_code == 201
    risposta = client.post("/desideri", json={"testo": "Un quarto regalo"}, headers=token)
    assert risposta.status_code == 403, "I desideri sono tre: al quarto, 403"
    assert risposta.json()["detail"] == "Hai finito i desideri"
    assert len(sql("SELECT id FROM desideri")) == 3


def test_livello_5_solo_i_miei():
    aladdin_id = padrone_nel_database()
    jasmine_id = padrone_nel_database("jasmine", "Jasmine", "tigre-rajah-1")
    desiderio_nel_database("Un palazzo", aladdin_id)
    desiderio_nel_database("Uscire dal palazzo", jasmine_id)
    desiderio_nel_database("Un elefante", aladdin_id)
    risposta = client.get("/desideri", headers=con_token(aladdin_id))
    assert risposta.status_code == 200, "Manca la rotta GET /desideri"
    assert [d["testo"] for d in risposta.json()] == ["Un palazzo", "Un elefante"], \
        "Ognuno vede solo i suoi desideri, in ordine di id: where padrone_id == padrone.id"


def test_livello_5_tre_a_testa():
    aladdin_id = padrone_nel_database()
    jasmine_id = padrone_nel_database("jasmine", "Jasmine", "tigre-rajah-1")
    for testo in ("Uno", "Due", "Tre"):
        desiderio_nel_database(f"Desiderio numero {testo}", jasmine_id)
    risposta = client.post("/desideri", json={"testo": "Un palazzo"}, headers=con_token(aladdin_id))
    assert risposta.status_code == 201, "Tre a testa: i desideri di Jasmine non consumano quelli di Aladdin"


def test_livello_5_ritiro_un_desiderio():
    aladdin_id = padrone_nel_database()
    desiderio_id = desiderio_nel_database("Un palazzo", aladdin_id)
    risposta = client.delete(f"/desideri/{desiderio_id}", headers=con_token(aladdin_id))
    assert risposta.status_code == 204, "Manca la rotta DELETE /desideri/{desiderio_id}, o il 204 nel decoratore"
    assert sql("SELECT id FROM desideri") == [], "Il desiderio è ancora nel database"


def test_livello_5_il_desiderio_di_un_altro():
    aladdin_id = padrone_nel_database()
    jasmine_id = padrone_nel_database("jasmine", "Jasmine", "tigre-rajah-1")
    di_jasmine = desiderio_nel_database("Uscire dal palazzo", jasmine_id)
    risposta = client.delete(f"/desideri/{di_jasmine}", headers=con_token(aladdin_id))
    assert risposta.status_code == 404, "Il desiderio di un altro, per me, non esiste: 404, come se non ci fosse"
    assert risposta.json()["detail"] == "Desiderio non trovato"
    assert len(sql("SELECT id FROM desideri")) == 1, "Il desiderio di Jasmine deve restare nel database"
    assert client.delete("/desideri/999", headers=con_token(aladdin_id)).status_code == 404


def test_livello_5_senza_token():
    assert client.post("/desideri", json={"testo": "Un palazzo"}).status_code == 401
    assert client.get("/desideri").status_code == 401
    assert client.delete("/desideri/1").status_code == 401


def test_livello_5_desiderio_troppo_corto():
    aladdin_id = padrone_nel_database()
    risposta = client.post("/desideri", json={"testo": "Eh"}, headers=con_token(aladdin_id))
    assert risposta.status_code == 422, "Il testo ha almeno 3 caratteri: Field(min_length=3)"


# ------------------------------------------------------------ livello 6 · le regole del Genio
def test_livello_6_niente_desideri_in_piu():
    aladdin_id = padrone_nel_database()
    token = con_token(aladdin_id)
    for testo in ("Voglio altri tre desideri", "Mille DESIDERI, grazie"):
        risposta = client.post("/desideri", json={"testo": testo}, headers=token)
        assert risposta.status_code == 400, "Se nel testo c'è la parola «desideri», maiuscola o minuscola: 400"
        assert risposta.json()["detail"] == "Il Genio non può: niente desideri in più"
    assert sql("SELECT id FROM desideri") == [], "Il desiderio vietato non deve finire nel database"


def test_livello_6_il_genio_esaudisce():
    aladdin_id = padrone_nel_database()
    genio_id = padrone_nel_database("genio", "Il Genio", "dieci-mila-anni", ruolo="genio")
    desiderio_id = desiderio_nel_database("Un palazzo", aladdin_id)
    risposta = client.put(f"/desideri/{desiderio_id}/esaudito", headers=con_token(genio_id))
    assert risposta.status_code == 200, "Manca la rotta PUT /desideri/{desiderio_id}/esaudito"
    assert risposta.json() == {"id": desiderio_id, "testo": "Un palazzo", "esaudito": True}
    assert sql("SELECT esaudito FROM desideri WHERE id = %s", (desiderio_id,)) == [{"esaudito": True}], \
        "Nel database il desiderio non è cambiato: c'è il db.commit()?"


def test_livello_6_solo_il_genio():
    aladdin_id = padrone_nel_database()
    desiderio_id = desiderio_nel_database("Un palazzo", aladdin_id)
    risposta = client.put(f"/desideri/{desiderio_id}/esaudito", headers=con_token(aladdin_id))
    assert risposta.status_code == 403, "Aladdin non è il Genio: so chi sei, ma non puoi. Serve ruolo in PadroneDB"
    assert risposta.json()["detail"] == "Solo il Genio esaudisce"
    assert sql("SELECT esaudito FROM desideri") == [{"esaudito": False}]


def test_livello_6_un_desiderio_che_non_esiste():
    genio_id = padrone_nel_database("genio", "Il Genio", "dieci-mila-anni", ruolo="genio")
    risposta = client.put("/desideri/999/esaudito", headers=con_token(genio_id))
    assert risposta.status_code == 404
    assert risposta.json()["detail"] == "Desiderio non trovato"
    assert client.put("/desideri/1/esaudito").status_code == 401, "Senza token: 401, come sempre"
