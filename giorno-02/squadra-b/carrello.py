import sys

def calcola(csv, codice_sconto):
    inventario = open(csv).read().split("\n")
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
                totale_lordo = prezzo * quantità 
                sconto_applicato = totale_lordo * 0.1
                totale_scontato = totale_lordo - sconto_applicato
                print(splitted[0] + " x" + str(quantità) + ": " + "%.2f" % sconto + " (-10%)")
            else:
                totale_scontato = totale_lordo
                print(splitted[0] + " x" + str(quantità) + ": " + "%.2f" % sconto)
            # aggiungo al totale
            totale += totale_scontato
        except:
            pass
    print("Subtotale: " + "%.2f" % totale)
    sconto = 0
    # controllo il codice
    if codice_sconto == "BENVENUTO":
        if totale >= 30:
            sconto = 5
            print("Codice BENVENUTO: -" + "%.2f" % sconto)
        else:
            print("Codice BENVENUTO: serve una spesa di almeno 30.00")
    elif codice_sconto == "SCONTO10":
        if totale >= 40:
            sconto = totale * 0.1
            print("Codice SCONTO10: -" + "%.2f" % sconto)
        else:
            print("Codice SCONTO10: serve una spesa di almeno 40.00")
    elif codice_sconto != "":
        print("Codice " + codice_sconto + " sconosciuto")
    t2 = totale - sconto
    # spedizione
    if t2 < 50:
        spedizione = 4.9
    else:
        spedizione = 0
    print("Spedizione: " + "%.2f" % spedizione)
    print("Totale: " + "%.2f" % (t2 + spedizione))

if len(sys.argv) > 2:
    calcola(sys.argv[1], sys.argv[2])
else:
    calcola(sys.argv[1], "")

#ciao 