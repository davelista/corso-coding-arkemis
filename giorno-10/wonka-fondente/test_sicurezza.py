"""I test delle funzioni di sicurezza.py (fondente). NON si modificano.

    pytest -v -k fondente_1      le password
    pytest -v -k fondente_2      il biglietto
"""
import os
from datetime import datetime, timezone

os.environ["SECRET_KEY"] = "chiave-solo-per-i-test-della-fabbrica-wonka"    # i test non leggono la vostra chiave

import jwt

from sicurezza import ALGORITMO, SECRET_KEY, calcola_hash, crea_biglietto, password_giusta


# ------------------------------------------------------------ F1 · le password
def test_fondente_1_l_impronta_non_e_la_password():
    impronta = calcola_hash("cioccolato")
    assert isinstance(impronta, str), "calcola_hash deve restituire l'impronta (una stringa): c'è il return?"
    assert impronta != "cioccolato", "L'impronta non può essere la password"


def test_fondente_1_ogni_volta_un_impronta_diversa():
    assert calcola_hash("cioccolato") != calcola_hash("cioccolato"), \
        "Due impronte della stessa password devono essere diverse: è il sale. Usate password_hash"


def test_fondente_1_password_giusta():
    impronta = calcola_hash("cioccolato")
    assert password_giusta("cioccolato", impronta) is True, "Con la password giusta: True"
    assert password_giusta("caramella", impronta) is False, "Con la password sbagliata: False"


# ------------------------------------------------------------ F2 · il biglietto
def test_fondente_2_il_biglietto_si_legge():
    biglietto = crea_biglietto(7)
    assert isinstance(biglietto, str), "crea_biglietto deve restituire il biglietto: c'è il return di jwt.encode?"
    try:
        dati = jwt.decode(biglietto, SECRET_KEY, algorithms=[ALGORITMO])
    except jwt.InvalidTokenError as errore:
        raise AssertionError(f"Il biglietto non si legge con SECRET_KEY e ALGORITMO: {errore}")
    assert dati["sub"] == "7", 'Dentro il biglietto, "sub" deve essere l\'id come testo: str(bambino_id)'


def test_fondente_2_il_biglietto_scade_tra_30_minuti():
    dati = jwt.decode(crea_biglietto(7), SECRET_KEY, algorithms=[ALGORITMO])
    assert "exp" in dati, 'Manca "exp": la scadenza'
    minuti = (dati["exp"] - datetime.now(timezone.utc).timestamp()) / 60
    assert 29 <= minuti <= 31, f"Il biglietto deve scadere tra 30 minuti (adesso + DURATA), non tra {minuti:.0f}"
