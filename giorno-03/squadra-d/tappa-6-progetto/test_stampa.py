from stampa import formatta_report


def test_il_report():
    atteso = "SPESE DELL'ANNO A HOGWARTS\ndolci: 51.50\ntreno: 49.00\nTOTALE: 100.50"
    assert formatta_report({"treno": 49.0, "dolci": 51.5}) == atteso


def test_ordine_alfabetico():
    testo = formatta_report({"zucca": 1.0, "bacchette": 2.0})
    righe = testo.split("\n")
    assert righe[1] == "bacchette: 2.00"
    assert righe[2] == "zucca: 1.00"


def test_nessuna_spesa():
    assert formatta_report({}) == "SPESE DELL'ANNO A HOGWARTS\nTOTALE: 0.00"
