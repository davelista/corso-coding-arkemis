from prezzo_biglietto import prezzo_biglietto


def test_gratis_fino_a_5_anni():
    assert prezzo_biglietto(0) == 0.0
    assert prezzo_biglietto(5) == 0.0


def test_ridotto_da_6_a_17():
    assert prezzo_biglietto(6) == 5.0
    assert prezzo_biglietto(17) == 5.0


def test_intero_da_18_a_64():
    assert prezzo_biglietto(18) == 10.0
    assert prezzo_biglietto(64) == 10.0


def test_over_65():
    assert prezzo_biglietto(65) == 6.0
    assert prezzo_biglietto(90) == 6.0
