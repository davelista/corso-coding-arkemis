# Tappa 6 · Il Club dei Duellanti

Fine dell'anno: Allock apre il Club dei Duellanti e Harry sfida Draco. Ogni incantesimo è una funzione: tre pezzi, uno a testa, che insieme raccontano il duello e dicono chi vince.

| Chi | Il tuo file | Il tuo branch | Nella storia |
|---|---|---|---|
| Numero 1 | `leggi.py` | `e-leggi` | Le mosse del duello |
| Numero 2 | `incantesimi.py` | `e-incantesimi` | Il libro degli incantesimi |
| Numero 3 | `annuncio.py` | `e-annuncio` | Chi vince? |

## Il programma

Al Club dei Duellanti, Harry e Draco si sfidano. Le mosse sono scritte in `duello.csv`, una per riga:

```text
turno,mago,bersaglio,incantesimo
1,Draco,Harry,stupeficium
2,Harry,Draco,expelliarmus
...
```

Le regole: tutti partono da **50 punti**. Ogni incantesimo toglie punti al bersaglio,
e i punti non vanno mai sotto zero. Un incantesimo che il libro non conosce fa cilecca: non toglie niente.

| Incantesimo | Punti tolti |
|---|---|
| expelliarmus | 10 |
| stupeficium | 20 |
| petrificus totalus | 30 |

**Un incantesimo è una funzione**: riceve i punti del bersaglio e restituisce (return) quelli che gli restano.

```python
def expelliarmus(punti):
    return punti - 10       # expelliarmus(50) -> 40
```

Il programma `duello.py` (già scritto, non si tocca) legge le mosse, lancia gli incantesimi e annuncia chi vince:

```text
$ python duello.py duello.csv
Turno 1: Draco lancia stupeficium su Harry, che resta con 30 punti
...
CLUB DEI DUELLANTI
Draco: 0 punti
Harry: 20 punti
VINCE: Harry
```

`duello.py` usa tre pezzi, uno per persona. Ognuno ha il suo test e può farlo diventare verde da solo.
`test_duello.py` invece è il test **di squadra**: diventa verde solo quando tutte e tre le PR sono sul branch della squadra.
Quando lo è: `git switch squadra-e-hogwarts`, `git pull` e `python duello.py duello.csv`.

I tre pezzi si passano i dati così:

```text
duello.csv ──leggi_mosse──▶ lista di mosse ──lancia (a ogni mossa)──▶ punti di ogni mago ──annuncia──▶ testo
```

Una mossa, cioè un elemento della lista di `leggi_mosse`, è fatta così:

```python
{"turno": 1, "mago": "Draco", "bersaglio": "Harry", "incantesimo": "stupeficium"}
```

## Se finite prima

- Scrivete il vostro duello in un file nuovo, per esempio `ron-hermione.csv`, e lanciatelo: `python duello.py ron-hermione.csv`.
- Aggiungete un incantesimo al libro: `rictusempra` (il solletico) toglie 5 punti. Ricordatevi di aggiungerlo anche in `lancia`.

## Come si fa

Sempre gli stessi passi. L'esempio è quello del numero 1 della squadra E: al posto del file e del branch mettete i vostri (sono nella tabella qui sopra).

**1. Il branch nuovo, preso dal branch della squadra**

```bash
git switch squadra-e-hogwarts
git pull
git switch -c e-leggi
cd ~/corso-coding-arkemis/giorno-03/squadra-e/tappa-6-progetto
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_leggi.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add leggi.py
git commit -m "Tappa 6: leggi"
git push -u origin e-leggi
```

**5. La pull request, verso il branch della squadra**

```bash
gh pr create --base squadra-e-hogwarts --fill
```

Oppure su GitHub: **Compare & pull request**, in alto cambia **base** da `main` a `squadra-e-hogwarts`, poi **Create pull request**.

**6. La review.** Apri la PR del compagno che ti tocca: un commento, **Approve**, poi **Merge pull request**.

## Se ti serve un aiuto

```python
with open(percorso) as file:          # apre il file e alla fine lo chiude da solo
    righe = file.read().splitlines()  # una lista di righe, senza "a capo"

righe[1:]                             # tutte tranne la prima (l'intestazione)
"1,Draco,Harry".split(",")            # ["1", "Draco", "Harry"]
turno, mago = ["1", "Draco"]          # spacchettare una lista in variabili
int("1")                              # 1: da testo a numero intero

for mago in sorted(punti):            # le chiavi in ordine alfabetico
    ...
"\n".join(["uno", "due"])             # "uno\ndue": unisce le righe con l'a capo
```
