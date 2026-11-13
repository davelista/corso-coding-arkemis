# Giorno 5 · Il giallo SQL e il tuo progetto

| Quando | Cartella | Cosa |
|---|---|---|
| 9:00 | questo README | Prendete il materiale e caricate i database |
| 10:05 | [`pirati/`](pirati/esercizi.md) | Dieci query sul diario di bordo dei Caraibi, con la correzione automatica |
| 10:40 | [`giallo/`](giallo/README.md) | **Il vagone fantasma della Linea Menta**: un giallo da risolvere con SQL, a squadre |
| 15:00 | [`progetto/`](progetto/README.md) | Il vostro progetto: il [canvas](progetto/CANVAS.md), la vostra app in una pagina |

Il bigino di SQL e il database `negozio` degli esempi sono nella cartella di ieri: [`giorno-04/BIGINO-SQL.md`](../giorno-04/BIGINO-SQL.md).

## Una volta sola: il materiale e i database

Dal terminale (su Windows: Ubuntu, WSL). Un comando alla volta.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-05
```

Se `git switch main` risponde «Your local changes would be overwritten»: scrivete `git stash` e rifate `git switch main`.

Poi i due database di oggi:

```bash
createdb pirati
psql -d pirati -f pirati/pirati.sql
createdb giallo
psql -d giallo -f giallo/giallo.sql
```

Se `createdb` risponde «already exists», va bene: il database c'è già, passate al comando dopo.

Per controllare: `psql -d pirati -c '\dt'` deve mostrare 2 tabelle, `psql -d giallo -c '\dt'` ne deve mostrare 13.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `connection refused` | PostgreSQL è spento. WSL: `sudo service postgresql start` · Mac: `brew services start postgresql@16` |
| `role "…" does not exist` | Rivedete il passo 5 della checklist del setup del giorno 1 |
| `No such file or directory` | Non siete nella cartella giusta: `cd ~/corso-coding-arkemis/giorno-05` |
