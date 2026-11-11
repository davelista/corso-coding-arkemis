from giudizio import giudizio


def test_insufficiente():
    assert giudizio(1) == "insufficiente"
    assert giudizio(5) == "insufficiente"


def test_sufficiente():
    assert giudizio(6) == "sufficiente"


def test_buono():
    assert giudizio(7) == "buono"
    assert giudizio(8) == "buono"


def test_ottimo():
    assert giudizio(9) == "ottimo"
    assert giudizio(10) == "ottimo"


def test_voti_fuori_scala():
    assert giudizio(0) == "voto non valido"
    assert giudizio(11) == "voto non valido"
