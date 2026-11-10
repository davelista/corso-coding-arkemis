from totale import totale


def test_somma_dei_prezzi():
    assert totale([10, 20, 5.5]) == 35.5


def test_i_negativi_si_ignorano():
    assert totale([10, -3, 2.5]) == 12.5


def test_lista_vuota():
    assert totale([]) == 0


def test_solo_negativi():
    assert totale([-1, -2]) == 0
