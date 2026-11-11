from indirizzo_gufo import indirizzo_gufo


def test_nome_e_cognome():
    assert indirizzo_gufo("Mario", "Rossi") == "mario.rossi@hogwarts.it"


def test_tutto_minuscolo():
    assert indirizzo_gufo("ANNA", "Bianchi") == "anna.bianchi@hogwarts.it"


def test_nomi_composti_senza_spazi():
    assert indirizzo_gufo("Anna Maria", "De Luca") == "annamaria.deluca@hogwarts.it"


def test_spazi_ai_lati():
    assert indirizzo_gufo(" Luca ", "Neri ") == "luca.neri@hogwarts.it"
