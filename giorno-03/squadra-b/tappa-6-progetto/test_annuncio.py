from annuncio import annuncia


def test_l_annuncio():
    atteso = "CLUB DEI DUELLANTI\nDraco: 0 punti\nHarry: 20 punti\nVINCE: Harry"
    assert annuncia({"Harry": 20, "Draco": 0}) == atteso


def test_ordine_alfabetico():
    righe = annuncia({"Ron": 10, "Hermione": 30, "Draco": 5}).split("\n")
    assert righe[1] == "Draco: 5 punti"
    assert righe[2] == "Hermione: 30 punti"
    assert righe[3] == "Ron: 10 punti"


def test_vince_chi_ha_piu_punti():
    righe = annuncia({"Ron": 10, "Hermione": 30, "Draco": 5}).split("\n")
    assert righe[-1] == "VINCE: Hermione"


def test_pareggio():
    righe = annuncia({"Ron": 10, "Hermione": 10}).split("\n")
    assert righe[-1] == "PAREGGIO"
