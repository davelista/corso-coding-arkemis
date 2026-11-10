# Tappa 6 · La fine dell'anno

Ultimo giorno prima delle vacanze: si fanno i conti dell'anno, in galeoni. Tre pezzi, uno a testa, che insieme fanno un programma vero.

| Chi | Il tuo file | Nella storia |
|---|---|---|
| Numero 1 | `leggi.py` | Leggere il registro delle spese |
| Numero 2 | `calcola.py` | I totali per categoria |
| Numero 3 | `stampa.py` | Il report di fine anno |

## Il programma

Durante l'anno a Hogwarts la squadra ha segnato le spese in `spese.csv`. Il programma `report.py` (già scritto, non si tocca) le legge e stampa il totale per categoria:

```text
$ python report.py spese.csv
SPESE DELL'ANNO A HOGWARTS
dolci: 51.50
pozioni: 15.00
treno: 49.00
TOTALE: 115.50
```

`report.py` usa tre funzioni, una per persona. Ognuno ha il suo test e può farlo diventare verde da solo.
`test_report.py` invece è il test **di squadra**: diventa verde solo quando tutte e tre le PR sono su main.
Quando lo è, fate `git switch main`, `git pull` e lanciate `python report.py spese.csv`.

I tre pezzi si passano i dati così:

```text
spese.csv ──leggi_spese──▶ lista di dizionari ──totali_per_categoria──▶ dizionario ──formatta_report──▶ testo
```

Un elemento della lista di `leggi_spese` è fatto così:

```python
{"data": "2026-09-01", "persona": "Harry", "categoria": "treno", "importo": 24.5}
```

## Come si fa

Sempre gli stessi passi. L'esempio è quello di Anna, numero 1 della squadra C: al posto di `anna` e del file mettete il vostro nome e il vostro file.

**1. Il branch nuovo**

```bash
git switch main
git pull
git switch -c c-anna-t6
cd ~/corso-coding-arkemis/giorno-03/squadra-c/tappa-6-progetto
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_leggi.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add leggi.py
git commit -m "Tappa 6: leggi"
git push -u origin c-anna-t6
```

**5. La pull request.** Su GitHub: **Compare & pull request**, poi **Create pull request**.

**6. La review.** Apri la PR del compagno che ti tocca: un commento, **Approve**, poi **Merge pull request**.

## Se ti serve un aiuto

```python
with open(percorso) as file:          # apre il file e alla fine lo chiude da solo
    righe = file.read().splitlines()  # una lista di righe, senza "a capo"

righe[1:]                             # tutte tranne la prima (l'intestazione)
"a,b,c".split(",")                    # ["a", "b", "c"]
data, persona = ["2026-09-01", "Harry"]  # spacchettare una lista in variabili

for categoria in sorted(totali):      # le chiavi in ordine alfabetico
    ...
"\n".join(["uno", "due"])             # "uno\ndue": unisce le righe con l'a capo
```
