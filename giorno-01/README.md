# Giorno 1 · La prima pull request

## Il laboratorio

1. Un branch con il vostro nome, in minuscolo: `git switch -c anna`
2. Un file solo vostro, `giorno-01/anna.md`, con tre cose: chi siete, che sistema usate, l'esito di `check_setup.py`
3. `git add giorno-01/anna.md` e `git commit -m "Aggiunge la presentazione di Anna"`
4. `git push -u origin anna`
5. `gh pr create --fill`, oppure il pulsante «Compare & pull request» su GitHub
6. Il compagno legge e approva; il merge lo fa il docente. Poi tutti: `git switch main` e `git pull`

## Extra: il conflitto

Due branch partono da `main` e cambiano la riga qui sotto in due modi diversi. Si uniscono uno dopo l'altro:
il secondo va in conflitto, e lo risolvete.

Mi chiamo ___ e uso ___
