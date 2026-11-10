# Tappa 2 · Il primo giorno

Primo giorno di scuola. Piton dà i voti alle pozioni, il Nottetempo fa pagare in base all'età e le sciarpe della casata si ordinano via gufo.

| Chi | Il tuo file | Nella storia |
|---|---|---|
| Numero 1 | `giudizio.py` | I voti di Piton |
| Numero 2 | `prezzo_biglietto.py` | Il biglietto del Nottetempo |
| Numero 3 | `spedizione.py` | Le sciarpe via gufo |

## Come si fa

Sempre gli stessi passi. L'esempio è quello di Anna, numero 1 della squadra A: al posto di `anna` e del file mettete il vostro nome e il vostro file.

**1. Il branch nuovo**

```bash
git switch main
git pull
git switch -c a-anna-t2
cd ~/corso-coding-arkemis/giorno-03/squadra-a/tappa-2-condizioni
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_giudizio.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add giudizio.py
git commit -m "Tappa 2: giudizio"
git push -u origin a-anna-t2
```

**5. La pull request.** Su GitHub: **Compare & pull request**, poi **Create pull request**.

**6. La review.** Apri la PR del compagno che ti tocca: un commento, **Approve**, poi **Merge pull request**.

## Se ti serve un aiuto

```python
if temperatura >= 35:
    stato = "caldo"
elif temperatura >= 20:      # si arriva qui solo se la prima è falsa
    stato = "bello"
else:
    stato = "fresco"

if 1 <= voto <= 10:          # "voto tra 1 e 10", estremi compresi
    ...
if eta < 6 or eta >= 65:     # or: basta una delle due
    ...
```

- `=` assegna, `==` confronta.
- L'ordine degli `elif` conta: Python si ferma al **primo** vero.
- Dopo `if`, `elif` ed `else` ci sono i due punti `:` e la riga sotto è rientrata di 4 spazi.
