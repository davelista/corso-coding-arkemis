import sys

def controlla(file):
    righe = open(file).read().splitlines()
    visti = []
    ok = 0
    tot = 0
    for i in range(1, len(righe)):
        try:
            a, b, c = righe[i].split(",")
        except:
            continue
        tot = tot + 1
        e = []
        # controllo lo username
        if len(a) < 3:
            e.append("username troppo corto")
        if len(a) > 15:
            e.append("username troppo lungo")
        for ch in a:
            if not (ch.isalnum() or ch == "_"):
                e.append("username con caratteri non ammessi")
                break
        if a.lower() in visti:
            e.append("username già usato")
        # controllo la email
        if b.count("@") != 1:
            e.append("email non valida")
        else:
            if "." not in b.split("@")[1]:
                e.append("email non valida")
        # controllo la password
        if len(c) < 8:
            e.append("password troppo corta")
        n = False
        for ch in c:
            if ch.isdigit():
                n = True
        if n == False:
            e.append("password senza numeri")
        if a.lower() in c.lower():
            e.append("password contiene lo username")
        if len(e) == 0:
            print("riga " + str(i + 1) + " " + a + ": OK")
            ok = ok + 1
            visti.append(a.lower())
        else:
            print("riga " + str(i + 1) + " " + a + ": " + "; ".join(e))
    print("Iscritti: " + str(ok) + " su " + str(tot))

controlla(sys.argv[1])
