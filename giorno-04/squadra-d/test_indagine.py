"""I test dell'indagine. Questo file NON si tocca.

pytest -v                  tutte le tappe
pytest -v -k tappa_3       solo la tappa 3
Verde = l'indizio di quella tappa è affidabile.
"""

import pytest

from indagine import (
    della_razza,
    entrati,
    fumatori,
    minuti,
    percorso,
    presenti,
    soste,
    cosa_dice,
)


def test_tappa_1_presenti():
    nomi = presenti()
    assert len(nomi) == 11
    assert nomi[:3] == ["Aragorn", "Bilbo", "Boromir"]


def test_tappa_2_cosa_dice():
    assert cosa_dice("Gimli").startswith("Ho dormito tutta la notte")


def test_tappa_2_chi_non_ha_testimoniato():
    assert cosa_dice("Boromir") == "Nessuna testimonianza"


def test_tappa_3_fumatori():
    assert fumatori() == ["Merry", "Pipino", "Bilbo", "Gandalf", "Aragorn", "Gimli"]


def test_tappa_4_della_razza():
    assert della_razza("elfo") == ["Legolas", "Elrond"]
    assert della_razza("nano") == ["Gimli"]


def test_tappa_5_percorso():
    assert percorso("Sam") == ["Camera di Frodo", "Cucine", "Camera di Frodo"]


def test_tappa_6_entrati():
    assert entrati("Cucine", "01:00", "02:00") == ["Sam", "Pipino"]


def test_tappa_6_ora_di_fine_esclusa():
    assert entrati("Camera di Frodo", "01:00", "01:20") == ["Pipino"]


def test_tappa_7_minuti():
    assert minuti("00:00") == 0
    assert minuti("01:40") == 100


@pytest.mark.parametrize("ora", ["verso le due", "25:00", "01:75"])
def test_tappa_7_ora_non_valida(ora):
    with pytest.raises(ValueError, match="Ora non valida"):
        minuti(ora)


def test_tappa_7_soste():
    assert soste("Sam") == {"Camera di Frodo": 75, "Cucine": 45}


def test_tappa_7_soste_con_un_ora_illeggibile(capsys):
    soste("Bilbo")  # non deve fermarsi
    assert "verso le due" in capsys.readouterr().err
