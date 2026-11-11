"""PROVA DEL DEBUGGER · 1 · Le gallette per il viaggio

Ogni membro della Compagnia mette nello zaino qualche lembas, le gallette degli elfi.
Quante sono in tutto? Dovrebbero essere 16. Il programma ne conta 12.
Nessun errore: il risultato è sbagliato e basta.

Mettete un breakpoint sulla riga «totale = 0» e seguite il ciclo un giro alla volta.
"""

zaini = {"Frodo": 3, "Sam": 5, "Merry": 2, "Pipino": 2, "Aragorn": 4}

nomi = list(zaini)
totale = 0
for i in range(len(nomi) - 1):
    nome = nomi[i]
    totale = totale + zaini[nome]

print("Lembas in tutto:", totale)
