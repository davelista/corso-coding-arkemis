from pathlib import Path

from leggi import leggi_mosse

PROVA = str(Path(__file__).parent / "prova.csv")


def test_legge_due_mosse():
    assert len(leggi_mosse(PROVA)) == 2


def test_la_prima_mossa():
    assert leggi_mosse(PROVA)[0] == {
        "turno": 1,
        "mago": "Ron",
        "bersaglio": "Hermione",
        "incantesimo": "expelliarmus",
    }


def test_il_turno_e_un_numero():
    assert leggi_mosse(PROVA)[1]["turno"] == 2


def test_incantesimo_con_lo_spazio():
    assert leggi_mosse(PROVA)[1]["incantesimo"] == "petrificus totalus"
