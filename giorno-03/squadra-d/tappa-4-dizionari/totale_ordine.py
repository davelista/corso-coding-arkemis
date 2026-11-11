"""HOGWARTS · Tappa 4 · Numero 2 · L'ordine al tavolo

La storia:  Burrobirra, succo di zucca, torta di melassa: con il menu e l'ordine del tavolo, quanto si paga? Il whisky incendiario ai minorenni non lo servono.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_totale_ordine.py -v     (tutto verde = finito)
"""


def totale_ordine(menu: dict[str, float], ordine: dict[str, int]) -> float:
    """Calcola il totale di un ordine: per ogni piatto, prezzo del menu per quantità.

    I piatti che non sono nel menu si ignorano.

    menu = {"burrobirra": 6.5, "succo di zucca": 1.5, "torta di melassa": 5.0}
    totale_ordine(menu, {"burrobirra": 2, "torta di melassa": 1})       ->  18.0
    totale_ordine(menu, {"whisky incendiario": 3, "succo di zucca": 1}) ->  1.5
    """


    
    """ piattiMenu = []
    prezzoPiattiMenu = []
    piattiOrdinati = []
    quantitàPiattiOrdinati = []

    for piatto, prezzo in menu.items():
        piattiMenu.append(piatto)
        prezzoPiattiMenu.append(prezzo)
        
    else:
        pass

    for ordine, quantità in ordine.items():
        if ordine in piattiMenu: """
    totale = 0
    for piattoOrdinato, quantità in ordine.items():
        if piattoOrdinato in menu:

            prezzoPiattoMenu = menu[piattoOrdinato]
            calcolo =  prezzoPiattoMenu * quantità
            totale = totale + calcolo

    return totale
            
# Questo blocco parte solo se lanciate il file: python totale_ordine.py
if __name__ == "__main__":
    print(totale_ordine({"burrobirra": 6.5, "succo di zucca": 1.5}, {"burrobirra": 2}))
