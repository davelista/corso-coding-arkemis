# Git · il giro, passo per passo

> **Come leggere i comandi**
> Le righe che iniziano con `$` sono comandi: scrivete quello che viene **dopo** il `$` e premete Invio.
> Quello che c'è dopo `#` è un commento per voi. Le righe senza `$` sono la risposta del terminale.

Oggi servono solo i comandi di questa pagina. Niente `git stash`, niente rebase: il giro, sempre lo stesso, finché diventa automatico.

Le quattro parole che servono:

| Parola | Cos'è |
|---|---|
| **commit** | Una foto salvata del vostro lavoro, con una frase che dice cosa è cambiato |
| **branch** | Una strada parallela: ci lavorate senza disturbare `main` e gli altri |
| **push** | Mandare i vostri commit su GitHub |
| **pull request (PR)** | La richiesta: «ho finito, controllate e unite il mio branch a `main`» |

---

## Il giro (uguale a ogni tappa)

### 1 · Ripartire da main aggiornato

```bash
$ git switch main
$ git pull
```

`git pull` scarica il lavoro che gli altri hanno già unito a `main`. Si fa **sempre** prima di un branch nuovo.

### 2 · Il branch nuovo

```bash
$ git switch -c a-anna-t1        # squadra a, Anna, tappa 1
Switched to a new branch 'a-anna-t1'
```

`-c` vuol dire «crea». Un branch nuovo per ogni tappa: mai lavorare su `main`.

### 3 · Il codice

```bash
$ cd squadra-a/tappa-1-stringhe  # dalla cartella giorno-03
$ code iniziali.py               # oppure apritelo da VS Code
```

Togliete `pass` e scrivete la funzione. Salvate (Cmd+S o Ctrl+S).

### 4 · I test

```bash
$ pytest test_iniziali.py -v
```

Rosso? Leggete la riga `assert`: dice cosa vi aspettavate e cosa è uscito. Correggete e rilanciate.
Andate avanti solo quando è tutto verde.

### 5 · Cosa è cambiato?

```bash
$ git status
On branch a-anna-t1
Changes not staged for commit:
        modified:   iniziali.py
```

Controllate due cose: il branch è il vostro (non `main`) e c'è **solo** il vostro file.

### 6 · Il commit

```bash
$ git add iniziali.py
$ git commit -m "Tappa 1: iniziali"
```

`git add` sceglie cosa mettere nella foto, `git commit` la scatta. Il messaggio dice cosa avete fatto, non «modifiche».

### 7 · Il push

```bash
$ git push -u origin a-anna-t1
```

`-u origin a-anna-t1` serve solo al primo push di un branch. Se poi correggete qualcosa, bastano `add`, `commit` e `git push`.

### 8 · La pull request

```bash
$ gh pr create --fill
```

Oppure su GitHub: compare il riquadro giallo **«Compare & pull request»**. Cliccate, controllate che sia `base: main` ← `compare: a-anna-t1`, e **Create pull request**.

Poi scrivete nella chat della squadra: «PR pronta» e il link.

---

## La review (la fa il compagno)

1. Aprite la PR del compagno: su GitHub, scheda **Pull requests**.
2. Scheda **Files changed**: leggete il codice. Si capisce? I nomi dicono cosa contengono? C'è un `return`? Le regole di ieri valgono anche oggi.
3. Passate sopra una riga e cliccate il **+** blu: scrivete **almeno un commento**. Una domanda («perché qui `<=`?») o un complimento con il motivo.
4. In alto a destra: **Review changes** → **Approve** → **Submit review**.
5. Tornate su **Conversation**: **Merge pull request** → **Confirm merge** → **Delete branch**.

Se c'è qualcosa da sistemare, al punto 4 scegliete **Request changes**. Chi ha scritto il codice corregge, fa `add`, `commit` e `git push` sullo **stesso branch**: la PR si aggiorna da sola.

---

## Il conflitto: il motto della squadra

Ultima tappa. Il motto della squadra va ricamato sulle sciarpe, e ognuno ha la sua proposta.
Stavolta il conflitto lo creiamo apposta, per imparare a risolverlo con calma.

**Tutti e tre**, ognuno sul suo branch, cambiano **la stessa riga** di `squadra-a/squadra.md`:

```bash
$ git switch main && git pull
$ git switch -c a-anna-motto
# in squadra.md: Motto: ancora da scegliere  →  Motto: il vostro motto
$ git add squadra.md
$ git commit -m "Propone un motto"
$ git push -u origin a-anna-motto
$ gh pr create --fill
```

Le PR si uniscono una alla volta. La prima entra liscia. Sulle altre GitHub scrive **«This branch has conflicts that must be resolved»**: due persone hanno cambiato la stessa riga e Git non sa chi ha ragione. Lo decidete voi.

Chi ha il conflitto:

```bash
$ git switch main
$ git pull                       # main con il motto già unito
$ git switch a-luca-motto        # il vostro branch
$ git merge main                 # portate main nel vostro branch
CONFLICT (content): Merge conflict in squadra-a/squadra.md
```

Aprite `squadra.md`. Git ha messo le due versioni una sopra l'altra:

```text
<<<<<<< HEAD
Motto: il motto di Luca
=======
Motto: il motto di Anna
>>>>>>> main
```

- Sopra `=======`: la vostra versione. Sotto: quella che è già su `main`.
- Decidete insieme il motto (anche un misto dei due), lasciate **una sola** riga `Motto: …` e cancellate le tre righe con `<<<<<<<`, `=======` e `>>>>>>>`.
- VS Code propone anche i pulsanti *Accept Current*, *Accept Incoming*, *Accept Both*: comodi, ma controllate sempre il risultato.

```bash
$ git add squadra.md             # «il conflitto è risolto»
$ git commit -m "Risolve il conflitto sul motto"
$ git push
```

La PR torna mergeable: il compagno la approva e la unisce. Poi tocca al terzo, che troverà un nuovo conflitto con il motto appena deciso. Alla fine il motto è uno solo, e l'avete scelto in tre.

---

## Guai frequenti

**«Dove sono? Su che branch sono?»**
`pwd` dice la cartella, `git status` il branch. Nel dubbio, sempre questi due.

**Ho modificato i file, ma sono su main.**
Nessun problema, se non avete ancora fatto commit: `git switch -c a-anna-t2`. Le modifiche vengono con voi sul branch nuovo.

**Ho fatto commit su main e il push viene rifiutato** (`protected branch`, `GH006`).
`main` è protetto: è giusto così. Create il branch da lì (`git switch -c a-anna-t2`): il commit viene con voi, poi `git push -u origin a-anna-t2`.
Poi rimettete a posto main: `git switch main` e `git reset --hard origin/main`. **Solo dopo** aver creato il branch, altrimenti il commit si perde.

**`git switch main` non parte: «Your local changes … would be overwritten».**
Avete modifiche non salvate in un commit. Finite il giro sul vostro branch (`add`, `commit`, `push`), poi cambiate.

**`git push` risponde «has no upstream branch».**
È il primo push del branch: usate il comando che vi suggerisce, `git push --set-upstream origin <branch>` (è lo stesso di `-u`).

**Il commit ha aperto una schermata strana.**
Avete dimenticato `-m "messaggio"`. Se in basso vedete `~` (è *vim*): premete Esc, scrivete `:wq` e Invio. Se vedete `^X Exit` (è *nano*): scrivete il messaggio, poi Ctrl+O, Invio, Ctrl+X.

**La PR contiene file di altri.**
Avete creato il branch senza `git switch main && git pull`, oppure partendo da un altro branch. Chiamate il docente prima di fare il merge.

**`cd ~/corso-coding-arkemis` risponde «No such file or directory».**
Avete clonato il repository da un'altra parte: `find ~ -maxdepth 3 -type d -name corso-coding-arkemis` vi dice dove. Usate quel percorso.

**`pytest: command not found` oppure `No module named pytest`.**
Il venv non è attivo: `source .venv/bin/activate` dalla cartella `giorno-03`.

**`ModuleNotFoundError: No module named 'iniziali'` oppure `import file mismatch`.**
Avete lanciato pytest dalla cartella sbagliata. Entrate nella cartella della tappa (`cd squadra-a/tappa-1-stringhe`) e lanciate solo il vostro test.

**`gh` chiede di fare login.**
Saltatelo: aprite il repository su GitHub e usate il riquadro **«Compare & pull request»**.
