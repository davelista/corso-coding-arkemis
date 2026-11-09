# Git Exercises · la guida passo passo

Git Exercises (<https://gitexercises.fracz.com>) è una palestra per Git: 23 esercizi da risolvere con il **Git vero**, nel tuo terminale. Ogni esercizio è una situazione da sistemare; quando pensi di avercela fatta, Git manda la tua soluzione al sito e il sito ti dice se è giusta.

Non serve un account. Serve solo Git (ce l'hai già) e una connessione a internet.

> **Come leggere i comandi di questa guida**
> Le righe che iniziano con `$` sono comandi: scrivi (o copia) quello che viene **dopo** il `$`, poi premi Invio.
> Tutto quello che c'è dopo `#` è un commento per te: non serve scriverlo.
> Le righe senza `$` sono quello che ti risponde il terminale.

---

## Passo 0 · Apri il terminale giusto

- **Windows**: apri **Ubuntu** (la finestra di WSL). Non PowerShell, non il Prompt dei comandi.
- **Mac**: apri il **Terminale**.

Vai nella tua cartella di casa e crea una cartella per oggi:

```bash
$ cd ~                    # ~ (tilde) vuol dire: la mia cartella di casa
$ pwd                     # dove sono?
/home/anna                # su Mac: /Users/anna
$ mkdir -p allenamento    # crea la cartella (se c'è già, non succede niente)
$ cd allenamento          # entra nella cartella
```

**Perché una cartella a parte?** Quello che scarichi è un repository Git. Non metterlo dentro la cartella del corso: un repository dentro un altro repository fa solo confusione.

**Se `pwd` risponde `/mnt/c/...`** sei nel disco di Windows: torna a casa con `cd ~`.

**Non trovi la tilde?** Scrivi solo `cd` e premi Invio: ti porta comunque a casa.

---

## Passo 1 · Scarica gli esercizi

```bash
$ git clone https://gitexercises.fracz.com/git/exercises.git
$ cd exercises
```

`git clone` copia sul tuo computer un repository che sta online, con tutta la sua storia. Alla fine trovi una cartella nuova, `exercises`: **da qui in poi tutti i comandi si danno lì dentro.**

> Copia l'indirizzo, non riscriverlo a mano: basta una lettera sbagliata e non funziona.
> In Ubuntu si incolla con **Ctrl+Shift+V** (o con il tasto destro del mouse), non con Ctrl+V.

---

## Passo 2 · Prepara il repository (una volta sola)

```bash
$ git status
```

**Se la prima riga dice `HEAD detached at ...`** non hai sbagliato niente: è la *HEAD staccata* (la HEAD non è appoggiata su un branch). Succede con questo repository. Torna su master:

```bash
$ git checkout master
```

Poi di' a Git chi sei, **solo per questo repository** (per questo non c'è `--global`):

```bash
$ git config user.name "un-nickname"
$ git config user.email "nickname@esempio.it"
```

- **Il nome è pubblico**: compare sulla home del sito, nella colonna *Latest solutions*, accanto agli esercizi risolti. Usa un nickname.
- **L'email può essere finta**: serve solo a riconoscere le tue soluzioni, non deve essere valida e non viene salvata.
- **Scorciatoia**: sulla home del sito ci sono due caselle, *Your name here* e *Your e-mail here*. Se le compili, i comandi sotto si aggiornano da soli e puoi copiarli tutti insieme.

Adesso lancia lo script che prepara tutto:

```bash
$ ./configure.sh
```

`./` vuol dire: esegui il file che sta in questa cartella. Lo script insegna a Git tre comandi nuovi, che di solito non esistono: **`git start`**, **`git verify`** e **`git exercises`**.

Infine prepara il primo esercizio:

```bash
$ git start
```

---

## Il giro di ogni esercizio: sempre quattro passi

| | Cosa fai | Comando |
|---|---|---|
| 1 | **Leggi** cosa chiede l'esercizio | `code README.md` oppure la pagina dell'esercizio su gitexercises.fracz.com |
| 2 | **Risolvi** con i comandi che conosci | `git status` prima e dopo ogni comando |
| 3 | **Verifica**: Git manda la soluzione al sito | `git verify` |
| 4 | Giusta? **Avanti**. Sbagliata? **Da capo** | `git start next` · `git start` |

- `git start` **senza niente dopo** rimette l'esercizio com'era all'inizio. Hai fatto un pasticcio? Non rattoppare: riparti.
- `git start nome-esercizio` ti porta a un esercizio preciso (per esempio `git start chase-branch`).
- `git exercises` mostra la lista di tutti gli esercizi, con quelli che hai già superato.
- `git verify` funziona con un push verso il sito: le righe che iniziano con `remote:` sono la risposta del sito, non errori.

---

## I primi due esercizi, insieme

**Esercizio 1 · `master`.** Non chiede niente: serve solo a provare `git verify`.

```bash
$ git verify
$ git start next          # passa al secondo esercizio
```

**Esercizio 2 · `commit-one-file`.** Ci sono due file nuovi, `A.txt` e `B.txt`: devi committarne **uno solo**.

```bash
$ git status              # A.txt e B.txt in rosso: sono sulla scrivania
$ git add A.txt           # metti sul set solo A.txt
$ git status              # A.txt è verde, B.txt è ancora rosso
$ git commit -m "Aggiunge A.txt"
$ git verify
$ git start next
```

Dal terzo in poi vai da solo, con gli stessi quattro passi.

---

## La mappa di oggi: i primi otto esercizi

| # | Esercizio | Cosa allena | Da ricordare |
|---|---|---|---|
| 1 | `master` | provare `git verify` | — |
| 2 | `commit-one-file` | committare un file solo | `git add` di quel file |
| 3 | `commit-one-file-staged` | togliere un file dal set | `git restore --staged` (online troverai anche `git reset HEAD`, il modo vecchio) |
| 4 | `ignore-them` | far finta che dei file non esistano | il file `.gitignore` |
| 5 | `chase-branch` | unire un branch | `git merge` |
| 6 | `merge-conflict` | risolvere un conflitto | i segni `<<<<<<<`, `=======`, `>>>>>>>`, poi `git add` e `git commit` |
| 7 | `save-your-work` | mettere da parte il lavoro senza committarlo | `git stash` |
| 8 | `change-branch-history` | spostare i commit su un'altra base | `git rebase`: ti metti sul branch da spostare |

**Per tutti**: dall'1 al 5. **Extra**: dal 6 all'8, poi `git start commit-parts`, che allena `git add -p`.

Gli altri esercizi (dal 9 al 23) sono più avanzati: puoi farli a casa, il sito si ricorda dove sei arrivato.

---

## Quando ti blocchi

**Non capisci cosa chiede.** Rileggi il README. Poi guarda com'è fatto il repository **prima** di toccarlo:

```bash
$ git status
$ git log --oneline --graph --all     # il grafo, con tutti i branch
```

Ricopia il grafo su un foglio, come su Mural.

**Hai fatto un pasticcio.** `git start` e si riparte da zero. Niente si è rotto.

**Git apre una schermata per scrivere un messaggio** (succede con merge e rebase). È un editor di testo, il messaggio è già scritto: devi solo salvare e uscire.

- **nano** (in basso vedi `^X Exit`): Ctrl+O, Invio, Ctrl+X
- **vim** (lo schermo è pieno di `~`): premi Esc, poi scrivi `:wq` e premi Invio

Per non vederli più, una volta sola:

```bash
$ git config --global core.editor "code --wait"
```

Da quel momento Git apre una scheda di VS Code: la chiudi e Git prosegue.

**Errori frequenti**

| Messaggio | Cosa vuol dire | Cosa fai |
|---|---|---|
| `./configure.sh: No such file or directory` | non sei nella cartella giusta | `cd ~/allenamento/exercises` |
| `./configure.sh: Permission denied` | il file non ha il permesso di esecuzione | `bash configure.sh` |
| `git: 'start' is not a git command` | non hai ancora lanciato lo script | `./configure.sh` |
| `HEAD detached at ...` | la HEAD non è su un branch | `git checkout master` |

Bloccato da dieci minuti? Scrivi in chat **il comando che hai dato e il messaggio che hai ricevuto**.
