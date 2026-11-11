# Tappa 0 · Mi presento
#
# 1. Copia questo file con il tuo nome, tutto minuscolo:   cp MODELLO.py anna.py
# 2. Nel tuo file cambia i valori delle quattro variabili (MODELLO.py non si tocca)
# 3. Lancialo:                                             python anna.py
# 4. Poi il giro di Git: branch, commit, push, pull request

nome = "Pierluigi"
citta = "Roma"
anni_di_python = 0
linguaggi = ["italiano", "inglese", "spagnolo", "Java"]  # tutti quelli che parli, anche quelli umani

print(f"Ciao, sono {nome}, vengo da {citta} e salgo sull'Hogwarts Express.")

if anni_di_python == 0:
    print("Python lo vedo per la prima volta.")
else:
    print(f"Uso Python da {anni_di_python} anni.")

print(f"Parlo {len(linguaggi)} linguaggi:")
for linguaggio in linguaggi:
    print(f"- {linguaggio}")
