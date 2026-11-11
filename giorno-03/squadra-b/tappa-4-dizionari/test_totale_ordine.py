from totale_ordine import totale_ordine

MENU = {"burrobirra": 6.5, "succo di zucca": 1.5, "torta di melassa": 5.0}


def test_totale_di_un_ordine():
    assert totale_ordine(MENU, {"burrobirra": 2, "torta di melassa": 1}) == 18.0


def test_i_piatti_che_non_ci_sono_si_ignorano():
    assert totale_ordine(MENU, {"whisky incendiario": 3, "succo di zucca": 1}) == 1.5


def test_ordine_vuoto():
    assert totale_ordine(MENU, {}) == 0
