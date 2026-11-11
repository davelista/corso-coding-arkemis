from iniziali import iniziali


def test_nome_e_cognome():
    assert iniziali("Mario", "Rossi") == "M.R."


def test_le_minuscole_diventano_maiuscole():
    assert iniziali("anna", "verdi") == "A.V."


def test_gli_spazi_ai_lati_non_contano():
    assert iniziali("  luca ", " neri") == "L.N."
