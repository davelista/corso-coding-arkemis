from riga_acquisto import riga_acquisto


def test_una_riga():
    assert riga_acquisto("piuma", 1.2, 3) == "piuma x3: 3.60 galeoni"


def test_un_pezzo_solo():
    assert riga_acquisto("calderone", 24.9, 1) == "calderone x1: 24.90 galeoni"


def test_il_prodotto_va_in_minuscolo():
    assert riga_acquisto("Pergamena", 2.5, 2) == "pergamena x2: 5.00 galeoni"
