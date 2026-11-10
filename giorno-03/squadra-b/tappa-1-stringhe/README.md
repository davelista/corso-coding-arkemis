# Tappa 1 · A Diagon Alley

È arrivata la lettera: si parte per Hogwarts. Prima del binario 9¾ c'è la spesa a Diagon Alley: le iniziali sui bauli, gli indirizzi per la posta via gufo e la cassa del Ghirigoro.

| Chi | Il tuo file | Nella storia |
|---|---|---|
| Numero 1 | `iniziali.py` | Le iniziali sui bauli |
| Numero 2 | `indirizzo_gufo.py` | La posta via gufo |
| Numero 3 | `riga_acquisto.py` | La cassa del Ghirigoro |

## Come si fa

Sempre gli stessi passi. L'esempio è quello di Anna, numero 1 della squadra B: al posto di `anna` e del file mettete il vostro nome e il vostro file.

**1. Il branch nuovo**

```bash
git switch main
git pull
git switch -c b-anna-t1
cd ~/corso-coding-arkemis/giorno-03/squadra-b/tappa-1-stringhe
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_iniziali.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add iniziali.py
git commit -m "Tappa 1: iniziali"
git push -u origin b-anna-t1
```

**5. La pull request.** Su GitHub: **Compare & pull request**, poi **Create pull request**.

**6. La review.** Apri la PR del compagno che ti tocca: un commento, **Approve**, poi **Merge pull request**.

## Se ti serve un aiuto

```python
nome = "  Anna Maria "
nome.strip()            # "Anna Maria"      toglie gli spazi ai lati
nome.lower()            # "  anna maria "   tutto minuscolo
nome.upper()            # "  ANNA MARIA "   tutto maiuscolo
nome.replace(" ", "")   # "AnnaMaria"       sostituisce (qui: toglie tutti gli spazi)
nome.strip()[0]         # "A"               il primo carattere
prezzo = 3.6
f"Totale: {prezzo:.2f}" # "Totale: 3.60"    f-string, con 2 decimali
```

I metodi si possono mettere in fila: `nome.strip().lower()`.
