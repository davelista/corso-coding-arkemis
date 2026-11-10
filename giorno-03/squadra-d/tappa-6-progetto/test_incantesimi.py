from incantesimi import expelliarmus, lancia, petrificus_totalus, stupeficium


def test_expelliarmus():
    assert expelliarmus(50) == 40


def test_stupeficium():
    assert stupeficium(50) == 30


def test_petrificus_totalus():
    assert petrificus_totalus(50) == 20


def test_mai_sotto_zero():
    assert stupeficium(15) == 0
    assert petrificus_totalus(20) == 0


def test_lancia_per_nome():
    assert lancia("expelliarmus", 50) == 40
    assert lancia("stupeficium", 50) == 30
    assert lancia("petrificus totalus", 50) == 20


def test_incantesimo_sconosciuto_fa_cilecca():
    assert lancia("serpensortia", 50) == 50
