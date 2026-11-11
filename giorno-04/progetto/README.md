# Il tuo progetto nasce oggi

Da oggi fino al Demo Day costruisci **una web app tua**: backend, database, interfaccia, login, test, online con un indirizzo pubblico. Oggi si parte dalla cosa più importante: **i dati**.

Regola d'oro: **piccolo e finito batte grande e a metà.** Meglio quattro tabelle fatte bene che dieci a metà.

## I passi di oggi

| Quando | Cosa |
|---|---|
| 15:30 | Scegli il dominio: uno della lista qui sotto, o una tua idea che rispetti i requisiti |
| 15:40 | Disegna lo schema nella tua sezione su Mural: tabelle, colonne, collegamenti |
| 16:10 | Revisione a coppie con la [checklist](checklist.md) |
| 16:20 – 16:50 | Il docente passa e valida. Finché non c'è il bollino **VALIDATO**, niente codice |
| 17:00 | Crei il tuo repository e scrivi `schema.sql` partendo da [schema-modello.sql](schema-modello.sql) |

Puoi cambiare idea sul dominio fino a domani alle 9:00. Dopo si costruisce.

## I domini proposti

| # | Dominio | In una frase |
|---|---|---|
| 1 | Biblioteca di condominio | Chi presta quale libro a chi, e quando deve tornare |
| 2 | Palestra | Corsi, orari, istruttori e iscrizioni ai corsi |
| 3 | Ricettario | Ricette con i loro ingredienti e le dosi; si cerca per ingrediente |
| 4 | Spese condivise | Gruppi di amici, spese comuni e chi deve quanto a chi |
| 5 | Tracker di abitudini | Abitudini da seguire e cosa hai fatto ogni giorno |
| 6 | Collezione | Vinili, libri o giochi da tavolo: cosa hai, a chi l'hai prestato, cosa vorresti |
| 7 | Eventi | Eventi con posti limitati e iscrizioni dei partecipanti |
| 8 | Prenotazione sale | Sale riunioni prenotabili a fasce orarie, senza sovrapposizioni |
| 9 | Officina | Clienti, veicoli e interventi fatti su ogni veicolo |
| 10 | Adozioni dal rifugio | Animali, richieste di adozione e visite |

## I requisiti minimi

- Una tabella **`utenti`**: serve per il login (giorno 7). È già nel modello.
- Almeno **tre tabelle** oltre a `utenti`.
- Almeno una relazione **uno a molti** (una chiave esterna).
- Almeno una relazione **molti a molti**, con la sua tabella ponte.
- Ogni tabella ha una **chiave primaria**.
- Almeno un vincolo che protegge i dati: `NOT NULL`, `UNIQUE` o `CHECK`.

## Il tuo repository

```bash
gh repo create progetto-<tuonome> --public --clone
cd progetto-<tuonome>
mkdir db
cp ../<repo-corso>/progetto/schema-modello.sql db/schema.sql
# scrivi le tue tabelle in db/schema.sql, poi:
createdb progetto
psql -d progetto -f db/schema.sql
git add db/schema.sql
git commit -m "Schema del database"
git push
```

Nel README del tuo repository scrivi, in tre righe: cosa fa l'app, per chi è, quali sono le tabelle.
