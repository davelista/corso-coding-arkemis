# Tappa 0 · Chi sale sull'Hogwarts Express?

Oggi la squadra vive il suo primo anno a Hogwarts, e ogni tappa della giornata è un momento dell'anno.
Prima di salire sul treno, la lista di chi c'è: ognuno scrive un piccolo programma che lo presenta.
Niente esercizi: serve a fare il giro di Git una volta, con calma, tutti insieme.

## Prima: i numeri

Nella stanza della squadra decidete chi è il numero 1, chi il 2 e chi il 3. Restano quelli per tutta la giornata.
Il **numero 1**, nella sua PR, scrive i tre nomi nella tabella di `squadra.md`. Gli altri non la toccano.

## I passi

```bash
git switch main
git pull
git switch -c d-anna-t0              # squadra, nome, tappa
cd ~/corso-coding-arkemis/giorno-03/squadra-d/tappa-0
cp MODELLO.py anna.py                # copia MODELLO.py in un file nuovo, anna.py
```

`cp` vuol dire *copy*, copia: il primo nome è il file da copiare, il secondo il file nuovo che nasce.
`MODELLO.py` resta com'è: d'ora in poi lavorate solo su `anna.py`.

1. Aprite `anna.py` (`code anna.py`), cambiate i valori delle quattro variabili e salvate.
2. Lanciatelo: `python anna.py`. Deve stampare la vostra presentazione.
3. Il lavoro va su GitHub:

```bash
git add anna.py
git commit -m "Tappa 0: anna"
git push -u origin d-anna-t0
```

4. Su GitHub: **Compare & pull request**, poi **Create pull request**.
5. Il compagno la legge, scrive un commento, **Approve** e **Merge pull request**.

Il giro completo, comando per comando: [GIT.md](../../GIT.md).
