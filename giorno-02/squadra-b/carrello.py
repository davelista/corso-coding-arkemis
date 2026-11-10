import sys

def calcola(f, c):
    r = open(f).read().split("\n")
    t = 0
    print("CARRELLO")
    # per ogni riga
    for x in r[1:]:
        if x == "":
            continue
        try:
            y = x.split(",")
            p = float(y[1])
            q = int(y[2])
            if q >= 3:
                tot = p * q - p * q * 0.1
                print(y[0] + " x" + str(q) + ": " + "%.2f" % tot + " (-10%)")
            else:
                tot = p * q
                print(y[0] + " x" + str(q) + ": " + "%.2f" % tot)
            # aggiungo al totale
            t = t + tot
        except:
            pass
    print("Subtotale: " + "%.2f" % t)
    s = 0
    # controllo il codice
    if c == "BENVENUTO":
        if t >= 30:
            s = 5
            print("Codice BENVENUTO: -" + "%.2f" % s)
        else:
            print("Codice BENVENUTO: serve una spesa di almeno 30.00")
    elif c == "SCONTO10":
        if t >= 40:
            s = t * 0.1
            print("Codice SCONTO10: -" + "%.2f" % s)
        else:
            print("Codice SCONTO10: serve una spesa di almeno 40.00")
    elif c != "":
        print("Codice " + c + " sconosciuto")
    t2 = t - s
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