# Tappa 4 · Ai Tre Manici di Scopa

Sabato a Hogsmeade. Burrobirra per tutti: si legge il menu, si contano le parole delle recensioni e si prepara la lista per il tavolo.

| Chi | Il tuo file | Nella storia |
|---|---|---|
| Numero 1 | `conta_parole.py` | Le recensioni della locanda |
| Numero 2 | `totale_ordine.py` | L'ordine al tavolo |
| Numero 3 | `per_iniziale.py` | La lista per il tavolo |

## Come si fa

Sempre gli stessi passi. L'esempio è quello di Anna, numero 1 della squadra C: al posto di `anna` e del file mettete il vostro nome e il vostro file.

**1. Il branch nuovo**

```bash
git switch main
git pull
git switch -c c-anna-t4
cd ~/corso-coding-arkemis/giorno-03/squadra-c/tappa-4-dizionari
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_conta_parole.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add conta_parole.py
git commit -m "Tappa 4: conta_parole"
git push -u origin c-anna-t4
```

**5. La pull request.** Su GitHub: **Compare & pull request**, poi **Create pull request**.

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
