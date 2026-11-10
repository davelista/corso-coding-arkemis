from spedizione import spedizione


def test_sotto_50_si_paga():
    assert spedizione(20, False) == 4.9
    assert spedizione(49.99, False) == 4.9


def test_da_50_in_su_gratis():
    assert spedizione(50, False) == 0.0
    assert spedizione(80, False) == 0.0


def test_express_sotto_50():
    assert spedizione(20, True) == 11.9


def test_express_si_paga_anche_sopra_50():
    assert spedizione(80, True) == 7.0
