# Giorno 3 · Un anno a Hogwarts

È arrivata la lettera: oggi la squadra vive il suo primo anno a Hogwarts. Ogni tappa della giornata è un momento dell'anno, e in ogni tappa ognuno scrive un piccolo programma che a Hogwarts servirebbe davvero: le iniziali sui bauli, il biglietto del Nottetempo, il conto ai Tre Manici di Scopa e, alla fine, un duello di magia.

Niente argomenti nuovi: ripassiamo Python facendo, e Git usandolo. Lo stesso giro a ogni tappa, finché non serve più guardare gli appunti.

## Una volta sola, la mattina

Prima si prepara il **venv** (*virtual environment*, ambiente virtuale): una cartella `.venv` con un Python e i pacchetti di questo solo progetto, oggi solo pytest.
Serve per tre motivi: ogni progetto ha le sue versioni dei pacchetti, il Python del computer resta pulito (su Ubuntu, fuori da un venv, `pip install` si rifiuta) e chiunque ricrea lo stesso ambiente con `requirements.txt`. La cartella `.venv` non va su GitHub.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-03
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Se `cd ~/corso-coding-arkemis` risponde «No such file or directory», avete clonato il repository da un'altra parte. Trovatelo con `find ~ -maxdepth 3 -type d -name corso-coding-arkemis` e usate quel percorso al posto di `~/corso-coding-arkemis`, anche nei README delle tappe.

Il prompt ora inizia con `(.venv)`. Se aprite un terminale nuovo: `cd ~/corso-coding-arkemis/giorno-03` e `source .venv/bin/activate`.

## Le regole

1. **Niente AI.** Copilot spento, niente chat. Se vi serve un aiuto: il [bigino](BIGINO.md), poi chiedete a me.
2. **Ognuno tocca solo il suo file.**
3. **Ogni esercizio: un branch nuovo e una pull request verso il branch della squadra** (`squadra-a-hogwarts`, `squadra-b-hogwarts`, …).
4. **Chi approva la PR fa anche il merge.** Su `main` unisce solo il docente, a fine giornata.

## Chi fa cosa

Ogni squadra ha la sua cartella (`squadra-a`, `squadra-b`, …) e tre numeri: 1, 2 e 3.
**I numeri li scegliete voi**, all'inizio della tappa 0, e restano quelli per tutto il giorno.
In ogni tappa ci sono tre esercizi: il numero 1 fa il primo, il 2 il secondo, il 3 il terzo.
Ogni squadra ha anche il suo branch su GitHub, `squadra-a-hogwarts` (o `-b-`, `-c-`…): è il «main» della squadra, e lì arrivano le vostre PR.

| Chi | Legge e approva la PR di |
|---|---|
| Numero 1 | numero 2 |
| Numero 2 | numero 3 |
| Numero 3 | numero 1 |

## La giornata

| Ora | Tappa | A Hogwarts |
|---|---|---|
| 10:15 | `tappa-0` | Chi sale sull'Hogwarts Express? Il primo giro di Git, tutti insieme |
| 10:55 | `tappa-1-stringhe` | A Diagon Alley |
| 11:50 | `tappa-2-condizioni` | Il primo giorno |
| 14:00 | `tappa-3-cicli` | A lezione |
| 14:45 | `tappa-4-dizionari` | Ai Tre Manici di Scopa |
| 15:40 | `tappa-5-errori` | Incantesimi andati storti |
| 16:20 | `tappa-6-progetto` | Il Club dei Duellanti: Harry contro Draco |
| 17:10 | `squadra.md` | Il motto per le sciarpe (e il conflitto, apposta) |

Ogni tappa ha il suo `README.md` con la storia e i passi, sempre gli stessi. Ogni file da completare ha in alto tre righe: **la storia**, **cosa fai**, **come provi**.

## Il giro, in breve

```bash
git switch squadra-a-hogwarts    # il branch della squadra
git pull
git switch -c a-iniziali         # il vostro: lettera della squadra e esercizio
# scrivete il codice, poi: pytest test_<vostro file>.py -v
git add iniziali.py              # solo il vostro file
git commit -m "Tappa 1: iniziali"
git push -u origin a-iniziali
gh pr create --base squadra-a-hogwarts --fill
```

La PR va **verso il branch della squadra**, non verso `main`. Se qualcosa va storto: [GIT.md](GIT.md), in fondo ci sono i guai più frequenti.

## Se finite prima

1. Leggete e approvate la PR che vi tocca.
2. Aiutate un compagno, solo a voce: la tastiera resta sua.
3. [Palestra](palestra/README.md): dieci esercizi in più.
