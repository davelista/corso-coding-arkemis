from solo_numeri import solo_numeri


def test_salta_quelli_che_non_sono_numeri():
    assert solo_numeri(["3", "ciao", "2.5", "", " 4 "]) == [3.0, 2.5, 4.0]


def test_tutti_numeri():
    assert solo_numeri(["1", "2"]) == [1.0, 2.0]


def test_nessun_numero():
    assert solo_numeri(["a", "b"]) == []
