from insufficienti import insufficienti


def test_trova_gli_insufficienti_in_ordine():
    assert insufficienti([7, 4, 6, 5, 9]) == [4, 5]


def test_il_6_non_e_insufficiente():
    assert insufficienti([6, 7]) == []


def test_lista_vuota():
    assert insufficienti([]) == []


def test_la_lista_originale_non_cambia():
    voti = [3, 8]
    assert insufficienti(voti) == [3]
    assert voti == [3, 8]
