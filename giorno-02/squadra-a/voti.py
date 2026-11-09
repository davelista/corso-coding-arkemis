import sys

f = open(sys.argv[1])
righe = f.readlines()
f.close()

d = {}
# ciclo sulle righe
for r in righe[1:]:
    if len(r.strip()) == 0:
        continue
    x = r.strip().split(",")
    if x[0] not in d:
        d[x[0]] = []
    try:
        v = float(x[2])
        # se il voto va bene lo aggiungo
        if v >= 1 and v <= 10:
            d[x[0]].append(v)
    except:
        pass

# stampa le medie
print("MEDIE")
tmp = []
for k in sorted(d):
    l = d[k]
    if len(l) == 0:
        print(k + ": n.d.")
    else:
        m = sum(l) / len(l)
        print(k + ": " + str(round(m, 2)) + " (" + str(len(l)) + " voti)")
        tmp.append((k, m))

# stampa gli insufficienti
print("INSUFFICIENTI")
n = 0
for k in sorted(d):
    l = d[k]
    if len(l) > 0:
        m = sum(l) / len(l)
        if m < 6:
            print("- " + k + " " + str(round(m, 2)))
            n = n + 1
if n == 0:
    print("nessuno")

# il migliore
b = None
bm = 0
for t in tmp:
    if t[1] > bm:
        b = t[0]
        bm = t[1]
print("MIGLIORE")
if b == None:
    print("nessuno")
else:
    print(b + " " + str(round(bm, 2)))
