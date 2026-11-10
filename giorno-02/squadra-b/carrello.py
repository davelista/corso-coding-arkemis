import sys

def calcola(f, c):
    inventario = open(f).read().split("\n")
    totale = 0
    print("CARRELLO")
    # scorro i prodotti
    for prodotto in inventario[1:]:
        if prodotto == "":
            continue
        try:
            splitted = prodotto.split(",")
            prezzo = float(splitted[1])
            quantità = int(splitted[2])
            if quantità >= 3:
                # applico lo sconto del 10%
                sconto = prezzo * quantità - prezzo * quantità * 0.1
                print(splitted[0] + " x" + str(quantità) + ": " + "%.2f" % sconto + " (-10%)")
            else:
                sconto = prezzo * quantità
                print(splitted[0] + " x" + str(quantità) + ": " + "%.2f" % sconto)
            # aggiungo al totale
            totale += sconto
        except:
            pass
    print("Subtotale: " + "%.2f" % totale)
    s = 0
    # controllo il codice
    if c == "BENVENUTO":
        if totale >= 30:
            s = 5
            print("Codice BENVENUTO: -" + "%.2f" % s)
        else:
            print("Codice BENVENUTO: serve una spesa di almeno 30.00")
    elif c == "SCONTO10":
        if totale >= 40:
            s = totale * 0.1
            print("Codice SCONTO10: -" + "%.2f" % s)
        else:
            print("Codice SCONTO10: serve una spesa di almeno 40.00")
    elif c != "":
        print("Codice " + c + " sconosciuto")
    t2 = totale - s
    # spedizione
    if t2 < 50:
        sp = 4.9
    else:
        sp = 0
    print("Spedizione: " + "%.2f" % sp)
    print("Totale: " + "%.2f" % (t2 + sp))

if len(sys.argv) > 2:
    calcola(sys.argv[1], sys.argv[2])
else:
    calcola(sys.argv[1], "")

#ciao 