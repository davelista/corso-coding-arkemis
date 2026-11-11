"""HOGWARTS · Tappa 2 · Numero 3 · Le sciarpe via gufo

La storia:  Le sciarpe della casata si ordinano per corrispondenza. Quanto costa il gufo? E il gufo espresso?

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_spedizione.py -v     (tutto verde = finito)
"""


def spedizione(totale: float, express: bool) -> float:
    """Restituisce il costo della spedizione.

    Spedizione normale: 4.90 se il totale è sotto 50, gratis (0.0) da 50 in su.
    Se express è True, si aggiungono sempre 7.00, anche quando la normale è gratis.

    spedizione(20, False)  ->  4.9
    spedizione(80, False)  ->  0.0
    spedizione(20, True)   ->  11.9
    spedizione(80, True)   ->  7.0
    """
    # pass al posto di pass: il vostro codice

    # Spedizione di base:
    if totale < 50:
        costo_spedizione = 4.90
    else:
        costo_spedizione = 0.0

    # Se l'utente ha scelto express, aggiungiamo SEMPRE! 7.00
    if express:
        costo_spedizione += 7.00

    return costo_spedizione




# Questo blocco parte solo se lanciate il file: python spedizione.py
if __name__ == "__main__":
    print(spedizione(20, True))
