from pathlib import Path

from leggi import leggi_spese

PROVA = str(Path(__file__).parent / "prova.csv")


def test_legge_tre_spese():
    assert len(leggi_spese(PROVA)) == 3


def test_la_prima_spesa():
    assert leggi_spese(PROVA)[0] == {
        "data": "2026-09-01",
        "persona": "Harry",
        "categoria": "treno",
        "importo": 24.5,
    }


def test_l_importo_e_un_numero():
    assert leggi_spese(PROVA)[2]["importo"] == 15.0
