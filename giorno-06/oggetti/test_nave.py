"""I test della palestra. NON si modificano: si modifica nave.py finché diventano verdi."""
from nave import Nave


def test_due_navi_due_biscotti():
    perla = Nave("Perla Nera", "Jack Sparrow", 32)
    empress = Nave("Empress", "Sao Feng", 24)
    assert perla.capitano == "Jack Sparrow"
    assert empress.capitano == "Sao Feng"


def test_descrivi():
    perla = Nave("Perla Nera", "Jack Sparrow", 32)
    assert perla.descrivi() == "Perla Nera, 32 cannoni"


def test_arrembaggio_aggiunge_al_bottino():
    perla = Nave("Perla Nera", "Jack Sparrow", 32)
    perla.arrembaggio(4200)
    perla.arrembaggio(6500)
    assert perla.bottino == 10700


def test_il_bottino_e_di_ogni_nave():
    perla = Nave("Perla Nera", "Jack Sparrow", 32)
    empress = Nave("Empress", "Sao Feng", 24)
    perla.arrembaggio(4200)
    assert empress.bottino == 0


def test_perde_cannoni():
    perla = Nave("Perla Nera", "Jack Sparrow", 32)
    perla.perde_cannoni(10)
    assert perla.cannoni == 22


def test_mai_sotto_zero():
    trader = Nave("Edinburgh Trader", "Capitano Bellamy", 12)
    trader.perde_cannoni(50)
    assert trader.cannoni == 0


def test_e_pericolosa():
    assert Nave("Olandese Volante", "Davy Jones", 46).e_pericolosa() is True
    assert Nave("Providence", "Hector Barbossa", 30).e_pericolosa() is False
