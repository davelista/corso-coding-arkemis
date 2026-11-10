import pytest

from dividi_conto import dividi_conto


def test_divisione_esatta():
    assert dividi_conto(100, 4) == 25.0


def test_arrotonda_a_due_decimali():
    assert dividi_conto(100, 3) == 33.33


def test_zero_persone():
    with pytest.raises(ValueError):
        dividi_conto(50, 0)


def test_persone_negative():
    with pytest.raises(ValueError):
        dividi_conto(50, -2)
