import sys

# variabili globali
MOL_QTA_ORD = 2
QTA_CONFEZIONE = 10
GIORNI_MIN_SCORTE = 3

# calcola la quantità da ordinare
def quantita_da_ordinare(scorta, soglia, moltiplicatore):
    return soglia * moltiplicatore - scorta

# calcola giorni di esaurimento scorte
def calcola_giorni_esaurimento(scorta, consumo):
    return scorta // consumo

# cacolo scorte del magazzino
def inventario_magazzino(dati_inventario):

    # lettura dati da csv e caricamento in array magazzino
    magazzino = []
    for riga_csv in open(dati_inventario).readlines()[1:]:
        try:
            codice, prodotto, scorta, soglia, consumo = riga_csv.strip().split(",")
            magazzino.append([codice, prodotto, int(scorta), int(soglia), int(consumo)])
        except ValueError:
            print("Errore nella lettura del csv")

    articoli_da_riordinare = []
    articoli_presenti = 0
    # destrutturazione per articolo
    for codice, prodotto, scorta, soglia, consumo in magazzino:
        # verifica se la quantità disponibile è inferiore alla soglia minima
        if scorta < soglia:
            qta_da_ordinare = quantita_da_ordinare(scorta, soglia, MOL_QTA_ORD)
            if qta_da_ordinare % QTA_CONFEZIONE != 0:
                qta_da_ordinare = qta_da_ordinare + (QTA_CONFEZIONE - qta_da_ordinare % QTA_CONFEZIONE)
            giorni_esaurimento_scorte = calcola_giorni_esaurimento(scorta, consumo)
            if giorni_esaurimento_scorte < GIORNI_MIN_SCORTE:
                articoli_da_riordinare.append(codice + " " + prodotto + ": scorta " + str(scorta) + ", soglia " + str(soglia) + ", ordina " + str(qta_da_ordinare) + " (URGENTE: " + str(giorni_esaurimento_scorte) + " giorni)")
            else:
                articoli_da_riordinare.append(codice + " " + prodotto + ": scorta " + str(scorta) + ", soglia " + str(soglia) + ", ordina " + str(qta_da_ordinare) + " (" + str(giorni_esaurimento_scorte) + " giorni)")
        else:
            articoli_presenti = articoli_presenti + 1
    
    # STAMPA DEL REPORT FINALE
    print("DA RIORDINARE")
    if len(articoli_da_riordinare) == 0:
        print("niente")
    for articolo in articoli_da_riordinare:
        print("- " + articolo)
    print("SCORTA SUFFICIENTE: " + str(articoli_presenti) + " prodotti")

# AVVIO DEL PROGRAMMA
inventario_magazzino(sys.argv[1])
