from per_iniziale import per_iniziale


def test_raggruppa_per_iniziale():
    nomi = ["Harry", "Ron", "hermione", "Neville", "Hagrid"]
    assert per_iniziale(nomi) == {
        "H": ["Harry", "hermione", "Hagrid"],
        "R": ["Ron"],
        "N": ["Neville"],
    }


def test_un_nome_solo():
    assert per_iniziale(["Dobby"]) == {"D": ["Dobby"]}


def test_lista_vuota():
    assert per_iniziale([]) == {}
