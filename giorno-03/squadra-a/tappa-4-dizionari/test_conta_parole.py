from conta_parole import conta_parole


def test_conta_le_parole():
    assert conta_parole("Il gufo e il gatto") == {"il": 2, "gufo": 1, "e": 1, "gatto": 1}


def test_maiuscole_e_minuscole_sono_uguali():
    assert conta_parole("Lumos LUMOS lumos") == {"lumos": 3}


def test_frase_vuota():
    assert conta_parole("") == {}
