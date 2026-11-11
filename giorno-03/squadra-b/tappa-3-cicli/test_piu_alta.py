from piu_alta import piu_alta


def test_trova_la_piu_alta():
    assert piu_alta([18.5, 22.0, 19.5]) == 22.0


def test_la_piu_alta_e_la_prima():
    assert piu_alta([30.0, 12.0, 15.5]) == 30.0


def test_tutte_sotto_zero():
    assert piu_alta([-3.0, -1.5, -7.0]) == -1.5


def test_un_giorno_solo():
    assert piu_alta([12.0]) == 12.0
