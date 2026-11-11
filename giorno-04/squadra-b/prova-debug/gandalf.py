"""PROVA DEL DEBUGGER · 2 · Lo zaino di Gandalf

Questa volta il programma si ferma con un errore.
Lanciatelo con il debugger SENZA breakpoint: VS Code si ferma da solo sulla riga
dell'errore, e nel pannello VARIABLES vedete com'erano le variabili in quel momento.
"""

zaini = {"Frodo": 3, "Sam": 5, "Merry": 2, "Pipino": 2, "Aragorn": 4}

compagnia = ["Frodo", "Sam", "Gandalf", "Aragorn"]
for nome in compagnia:
    print(nome, "porta", zaini[nome], "lembas")
