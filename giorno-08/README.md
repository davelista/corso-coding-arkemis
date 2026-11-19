# Giorno 8 · Il colpo, passo per passo

Oggi niente cartelle nuove: si lavora nella cartella di ieri, `giorno-07`, con lo stesso venv.
Il colpo lo risolviamo insieme, un livello alla volta; poi la banda da soli; poi il database.

| Quando | Cartella | Cosa |
|---|---|---|
| 9:50 | [`../giorno-07/colpo/`](../giorno-07/colpo/README.md) | **Il colpo, passo per passo**: sette livelli e la cassaforte, tutti insieme |
| 14:40 | [`../giorno-07/banda/`](../giorno-07/banda/README.md) | **La banda, da soli**: POST, PUT e DELETE |
| 15:50 | [`../giorno-07/villa-db/`](../giorno-07/villa-db/README.md) | **La villa su PostgreSQL**: i dati che restano |

## Ogni mattina

Dal terminale (su Windows: Ubuntu, WSL). Un comando alla volta.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-07
source .venv/bin/activate
```

Avete scritto codice ieri sul vostro branch e non l'avete ancora salvato? Prima di `git switch main`, salvatelo lì:

```bash
git add .
git commit -m "colpo: fin dove sono arrivato"
```

La prova: `cd colpo` e poi `fastapi dev main.py`. Aprite **http://127.0.0.1:8000/docs**: vedete l'API della villa? Siete pronti.

## Le soluzioni

Arrivano in [`soluzioni/`](soluzioni/) a fine giornata: il colpo e la banda, scritti come li abbiamo scritti insieme.
