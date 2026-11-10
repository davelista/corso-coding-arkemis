# Tappa 4 · Ai Tre Manici di Scopa

Sabato a Hogsmeade. Burrobirra per tutti: si legge il menu, si contano le parole delle recensioni e si prepara la lista per il tavolo.

| Chi | Il tuo file | Il tuo branch | Nella storia |
|---|---|---|---|
| Numero 1 | `conta_parole.py` | `b-conta-parole` | Le recensioni della locanda |
| Numero 2 | `totale_ordine.py` | `b-totale-ordine` | L'ordine al tavolo |
| Numero 3 | `per_iniziale.py` | `b-per-iniziale` | La lista per il tavolo |

## Come si fa

Sempre gli stessi passi. L'esempio è quello del numero 1 della squadra B: al posto del file e del branch mettete i vostri (sono nella tabella qui sopra).

**1. Il branch nuovo, preso dal branch della squadra**

```bash
git switch squadra-b-hogwarts
git pull
git switch -c b-conta-parole
cd ~/corso-coding-arkemis/giorno-03/squadra-b/tappa-4-dizionari
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_conta_parole.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add conta_parole.py
git commit -m "Tappa 4: conta_parole"
git push -u origin b-conta-parole
```

**5. La pull request, verso il branch della squadra**

```bash
gh pr create --base squadra-b-hogwarts --fill
```

Oppure su GitHub: **Compare & pull request**, in alto cambia **base** da `main` a `squadra-b-hogwarts`, poi **Create pull request**.

**6. La review.** Apri la PR del compagno che ti tocca: un commento, **Approve**, poi **Merge pull request**.

## Se ti serve un aiuto

```python
menu = {"burrobirra": 6.5, "acqua": 1.5}   # chiave: valore
menu["burrobirra"]                         # 6.5
menu["torta"] = 5.0                        # aggiunge (o sovrascrive) una chiave
"acqua" in menu                            # True: la chiave c'è?

for piatto, prezzo in menu.items():        # chiave e valore insieme
    print(piatto, prezzo)

conteggi = {}
parola = "ciao"
if parola in conteggi:
    conteggi[parola] = conteggi[parola] + 1
else:
    conteggi[parola] = 1                  # la prima volta la chiave non c'è

"Il gufo".lower().split()                 # ["il", "gufo"]: una lista di parole
```
