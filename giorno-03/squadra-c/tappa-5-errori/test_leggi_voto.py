import pytest

from leggi_voto import leggi_voto


def test_un_voto_valido():
    assert leggi_voto("7") == 7


def test_gli_spazi_non_contano():
    assert leggi_voto(" 10 ") == 10


def test_non_e_un_numero():
    with pytest.raises(ValueError):
        leggi_voto("sette")


def test_troppo_alto():
    with pytest.raises(ValueError):
        leggi_voto("11")


def test_troppo_basso():
    with pytest.raises(ValueError):
        leggi_voto("0")
