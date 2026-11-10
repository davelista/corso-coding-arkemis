import sys

def inventario_magazzino(dati_inventario):
    magazzino = []
    for riga_csv in open(dati_inventario).readlines()[1:]:
        try:
            codice, prodotto, scorta, soglia, consumo = riga_csv.strip().split(",")
            magazzino.append([codice, prodotto, int(scorta), int(soglia), int(consumo)])
        except:
            pass
    articoli_da_riordinare = []
    articoli_presenti = 0
    for codice, prodotto, scorta, soglia, consumo in magazzino:
        # se è sotto la soglia
        if scorta < soglia:
            qta_da_ordinare = soglia * 2 - scorta
            if qta_da_ordinare % 10 != 0:
                qta_da_ordinare = qta_da_ordinare + (10 - qta_da_ordinare % 10)
            giorni_esaurimento_scorte = scorta // consumo
            if giorni_esaurimento_scorte < 3:
                articoli_da_riordinare.append(codice + " " + prodotto + ": scorta " + str(scorta) + ", soglia " + str(soglia) + ", ordina " + str(qta_da_ordinare) + " (URGENTE: " + str(giorni_esaurimento_scorte) + " giorni)")
            else:
                articoli_da_riordinare.append(codice + " " + prodotto + ": scorta " + str(scorta) + ", soglia " + str(soglia) + ", ordina " + str(qta_da_ordinare) + " (" + str(giorni_esaurimento_scorte) + " giorni)")
        else:
            articoli_presenti = articoli_presenti + 1
    print("DA RIORDINARE")
    if len(articoli_da_riordinare) == 0:
        print("niente")
    for articolo in articoli_da_riordinare:
        print("- " + articolo)
    print("SCORTA SUFFICIENTE: " + str(articoli_presenti) + " prodotti")

inventario_magazzino(sys.argv[1])
