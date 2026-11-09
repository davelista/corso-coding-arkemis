import sys

def elabora(p):
    l = []
    for riga in open(p).readlines()[1:]:
        try:
            c = riga.strip().split(",")
            l.append([c[0], c[1], int(c[2]), int(c[3]), int(c[4])])
        except:
            pass
    r = []
    ok = 0
    for x in l:
        # se è sotto la soglia
        if x[2] < x[3]:
            q = x[3] * 2 - x[2]
            if q % 10 != 0:
                q = q + (10 - q % 10)
            g = x[2] // x[4]
            if g < 3:
                r.append(x[0] + " " + x[1] + ": scorta " + str(x[2]) + ", soglia " + str(x[3]) + ", ordina " + str(q) + " (URGENTE: " + str(g) + " giorni)")
            else:
                r.append(x[0] + " " + x[1] + ": scorta " + str(x[2]) + ", soglia " + str(x[3]) + ", ordina " + str(q) + " (" + str(g) + " giorni)")
        else:
            ok = ok + 1
    print("DA RIORDINARE")
    if len(r) == 0:
        print("niente")
    for y in r:
        print("- " + y)
    print("SCORTA SUFFICIENTE: " + str(ok) + " prodotti")

elabora(sys.argv[1])
