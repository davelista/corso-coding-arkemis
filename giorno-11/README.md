# Giorno 11 · La lampada di Agrabah, e il frontend

Il backend si chiude, il frontend comincia. La mattina l'aula si divide in due strade, tutte e due ad Agrabah. Il pomeriggio, tutti insieme: React.

| Quando | Cartella | Per chi | Cosa |
|---|---|---|---|
| 9:50 | [`agrabah/`](agrabah/README.md) | Gruppo backend | **La lampada di Agrabah**: un'API da zero, senza funzioni pronte. I tesori, la chiave, il login, i desideri |
| 9:50 | [`bazar/`](bazar/README.md) | Gruppo web | **Il bazar**: la pagina dei tesori, in HTML, CSS e JavaScript |
| 14:00 | [`react/`](react/README.md) | Tutti | **Il bazar, in React**: la stessa pagina, ricreata a componenti, con Next.js e Tailwind |

## Una volta sola: il materiale di oggi

Dal terminale (su Windows: Ubuntu, WSL). Un comando alla volta.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-11
```

Se `git switch main` risponde «Your local changes would be overwritten»: scrivete `git stash` e rifate `git switch main`.

Poi ognuno va nella sua cartella: il resto è nel README di quella cartella.

- **Gruppo backend:** serve il venv, come venerdì. I comandi sono in [`agrabah/README.md`](agrabah/README.md).
- **Gruppo web:** stamattina non serve nessun venv. Bastano VS Code e il browser.
- **Per il pomeriggio, tutti:** `node --version` deve rispondere `v22` o più. Lo controlliamo prima di pranzo.
