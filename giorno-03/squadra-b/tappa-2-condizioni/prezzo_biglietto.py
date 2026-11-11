"""HOGWARTS · Tappa 2 · Numero 2 · Il biglietto del Nottetempo

La storia:  Il Nottetempo, l'autobus dei maghi, fa pagare in base all'età: piccoli gratis, ragazzi ridotto, maghi anziani scontato.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_prezzo_biglietto.py -v     (tutto verde = finito)
"""


def prezzo_biglietto(eta: int) -> float:
    """Restituisce il prezzo del biglietto in base all'età.

    da 0 a 5 anni     ->  0.0    (gratis)
    da 6 a 17 anni    ->  5.0    (ridotto)
    da 18 a 64 anni   ->  10.0   (intero)
    da 65 anni in su  ->  6.0    (over 65)
    """
    if eta < 0:
        return None
    
    prezzo_biglietto= 0.0
    if 0<= eta < 6:
        prezzo_biglietto += 0.0
    elif 6<= eta < 18:
        prezzo_biglietto += 5.0
    elif 18<= eta < 65:
        prezzo_biglietto += 10.0
    else:
        prezzo_biglietto += 6.0
    return prezzo_biglietto
        


# Questo blocco parte solo se lanciate il file: python prezzo_biglietto.py
if __name__ == "__main__":
    print(prezzo_biglietto(30))
