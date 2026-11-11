def riga_acquisto(prodotto: str, prezzo: float, quantita: int) -> str:
    """Restituisce la riga dell'acquisto: prodotto in minuscolo, quantità e totale in galeoni con 2 decimali.

    riga_acquisto("piuma", 1.2, 3)       ->  "piuma x3: 3.60 galeoni"
    riga_acquisto("Pergamena", 2.5, 2)   ->  "pergamena x2: 5.00 galeoni"
    """
    prodotto_minuscolo = prodotto.lower()
    totale = prezzo * quantita
    return prodotto_minuscolo + " x" + str(quantita) + ": " + format(totale, ".2f") + " galeoni"
# Questo blocco parte solo se lanciate il file: python riga_acquisto.py
if __name__ == "__main__":
    print(riga_acquisto("piuma", 1.2, 3))
