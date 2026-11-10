import sys

def report(nome):
    dati = {}
    an = []
    f = open(nome)
    f.readline()
    for riga in f:
        try:
            r = riga.strip().split(",")
            lo = float(r[2])
            hi = float(r[3])
            if lo > hi:
                continue
            if r[1] not in dati:
                dati[r[1]] = []
            dati[r[1]].append((r[0], lo, hi))
            # controllo se è anomala
            if hi - lo > 15 or hi >= 35:
                an.append(r[0] + " " + r[1] + ": min " + "%.1f" % lo + ", max " + "%.1f" % hi)
        except:
            pass
    f.close()
    for c in sorted(dati):
        print(c.upper())
        # minima
        m = dati[c][0]
        for g in dati[c]:
            if g[1] < m[1]:
                m = g
        print("  minima: " + "%.1f" % m[1] + " il " + m[0])
        # massima
        m = dati[c][0]
        for g in dati[c]:
            if g[2] > m[2]:
                m = g
        print("  massima: " + "%.1f" % m[2] + " il " + m[0])
        # escursione
        s = 0
        for g in dati[c]:
            s = s + (g[2] - g[1])
        print("  escursione media: " + "%.1f" % (s / len(dati[c])))
    print("GIORNATE ANOMALE")
    if len(an) == 0:
        print("nessuna")
    for x in sorted(an):
        print("- " + x)

report(sys.argv[1])
