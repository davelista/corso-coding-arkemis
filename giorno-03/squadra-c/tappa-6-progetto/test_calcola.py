from calcola import totali_per_categoria


def spesa(categoria, importo):
    return {"data": "2026-09-01", "persona": "Harry", "categoria": categoria, "importo": importo}


def test_somma_per_categoria():
    spese = [spesa("treno", 24.5), spesa("dolci", 18.0), spesa("treno", 24.5)]
    assert totali_per_categoria(spese) == {"treno": 49.0, "dolci": 18.0}


def test_una_spesa_sola():
    assert totali_per_categoria([spesa("pozioni", 15.0)]) == {"pozioni": 15.0}


def test_nessuna_spesa():
    assert totali_per_categoria([]) == {}
