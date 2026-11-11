# Tappa 3 · A lezione

Le prime settimane: la cassa comune delle Cioccorane (con Pix che fa scherzi), i voti bassi in Trasfigurazione e il freddo del Lago Nero a gennaio.

| Chi | Il tuo file | Il tuo branch | Nella storia |
|---|---|---|---|
| Numero 1 | `totale.py` | `b-totale` | La cassa delle Cioccorane |
| Numero 2 | `insufficienti.py` | `b-insufficienti` | Ripetizioni da Hermione |
| Numero 3 | `piu_alta.py` | `b-piu-alta` | Il Lago Nero a gennaio |

## Come si fa

Sempre gli stessi passi. L'esempio è quello del numero 1 della squadra B: al posto del file e del branch mettete i vostri (sono nella tabella qui sopra).

**1. Il branch nuovo, preso dal branch della squadra**

```bash
git switch squadra-b-hogwarts
git pull
git switch -c b-totale
cd ~/corso-coding-arkemis/giorno-03/squadra-b/tappa-3-cicli
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_totale.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add totale.py
git commit -m "Tappa 3: totale"
git push -u origin b-totale
```

**5. La pull request, verso il branch della squadra**

```bash
gh pr create --base squadra-b-hogwarts --fill
```

Oppure su GitHub: **Compare & pull request**, in alto cambia **base** da `main` a `squadra-b-hogwarts`, poi **Create pull request**.

**6. La review.** Apri la PR del compagno che ti tocca: un commento, **Approve**, poi **Merge pull request**.

## Se ti serve un aiuto

```python
voti = [7, 4, 6]
for voto in voti:            # voto vale 7, poi 4, poi 6
    print(voto)

somma = 0                    # 1. si parte da un valore
for voto in voti:
    somma = somma + voto     # 2. a ogni giro si aggiorna
print(somma)                 # 3. alla fine (fuori dal for!) si usa: 17

bassi = []                   # una lista vuota
bassi.append(4)              # aggiunge in fondo: [4]
len(voti)                    # 3, quanti elementi
voti[0]                      # 7, il primo (si conta da 0)
```

Oggi niente `sum()`, `max()` o `min()`: l'allenamento è proprio scrivere il ciclo.
