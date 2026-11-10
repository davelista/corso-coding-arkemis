# Tappa 1 · A Diagon Alley

È arrivata la lettera: si parte per Hogwarts. Prima del binario 9¾ c'è la spesa a Diagon Alley: le iniziali sui bauli, gli indirizzi per la posta via gufo e la cassa del Ghirigoro.

| Chi | Il tuo file | Il tuo branch | Nella storia |
|---|---|---|---|
| Numero 1 | `iniziali.py` | `e-iniziali` | Le iniziali sui bauli |
| Numero 2 | `indirizzo_gufo.py` | `e-indirizzo-gufo` | La posta via gufo |
| Numero 3 | `riga_acquisto.py` | `e-riga-acquisto` | La cassa del Ghirigoro |

## Come si fa

Sempre gli stessi passi. L'esempio è quello del numero 1 della squadra E: al posto del file e del branch mettete i vostri (sono nella tabella qui sopra).

**1. Il branch nuovo, preso dal branch della squadra**

```bash
git switch squadra-e-hogwarts
git pull
git switch -c e-iniziali
cd ~/corso-coding-arkemis/giorno-03/squadra-e/tappa-1-stringhe
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_iniziali.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add iniziali.py
git commit -m "Tappa 1: iniziali"
git push -u origin e-iniziali
```

**5. La pull request, verso il branch della squadra**

```bash
gh pr create --base squadra-e-hogwarts --fill
```

Oppure su GitHub: **Compare & pull request**, in alto cambia **base** da `main` a `squadra-e-hogwarts`, poi **Create pull request**.

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
