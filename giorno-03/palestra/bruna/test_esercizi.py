from esercizi import (
    conta_vocali,
    conto_alla_rovescia,
    dopo_le_vendite,
    inverti,
    media,
    palindromo,
    pari_o_dispari,
    parola_piu_lunga,
    pizza_pasta,
    tabellina,
)


def test_01_pari_o_dispari():
    assert pari_o_dispari(4) == "pari"
    assert pari_o_dispari(7) == "dispari"
    assert pari_o_dispari(0) == "pari"


def test_02_inverti():
    assert inverti("ciao") == "oaic"
    assert inverti("") == ""


def test_03_conto_alla_rovescia():
    assert conto_alla_rovescia(3) == [3, 2, 1]
    assert conto_alla_rovescia(0) == []


def test_04_tabellina():
    assert tabellina(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


def test_05_conta_vocali():
    assert conta_vocali("Ciao Anna") == 5
    assert conta_vocali("xyz") == 0


def test_06_media():
    assert media([6, 7, 8]) == 7.0
    assert media([]) == 0.0


def test_07_parola_piu_lunga():
    assert parola_piu_lunga("il gatto mangia") == "mangia"
    assert parola_piu_lunga("uno due tre") == "uno"


def test_08_palindromo():
    assert palindromo("Anna") is True
    assert palindromo("I topi non avevano nipoti") is True
    assert palindromo("Python") is False


def test_09_pizza_pasta():
    assert pizza_pasta(9) == "pizza"
    assert pizza_pasta(10) == "pasta"
    assert pizza_pasta(15) == "pizzapasta"
    assert pizza_pasta(7) == "7"


def test_10_dopo_le_vendite():
    magazzino = {"penna": 5, "zaino": 2}
    assert dopo_le_vendite(magazzino, ["penna", "penna", "zaino"]) == {"penna": 3, "zaino": 1}
    assert magazzino == {"penna": 5, "zaino": 2}
