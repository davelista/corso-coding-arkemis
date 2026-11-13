# Il tuo progetto nasce oggi

Da oggi fino al Demo Day costruisci **una web app tua**: database, backend, interfaccia, login, test, online con un indirizzo pubblico. Ogni lezione aggiunge un pezzo alla stessa app.

Regola d'oro: **piccolo e finito batte grande e a metà.** Meglio tre funzioni fatte bene che dieci a metà.

## Come cresce il progetto

| Passo | Cosa fai |
|---|---|
| Oggi | **L'idea**: compili il [canvas](CANVAS.md), la tua app in una pagina |
| Poi | **I dati**: le tabelle nel file `schema.sql`, con la [checklist](checklist.md) |
| Poi | Le API con FastAPI, collegate al database |
| Poi | Login e permessi |
| Poi | Online, con un indirizzo pubblico |
| Poi | L'interfaccia in React |
| Giorno 19 | Test, rifinitura e Demo Day |

## Oggi, passo per passo

| Quando | Cosa |
|---|---|
| 15:00 | Il docente spiega il canvas, con un esempio |
| 15:25 | Scegli il dominio: uno della lista qui sotto, o una tua idea |
| 15:25 – 16:10 | Da solo: compili gli otto riquadri del [canvas](CANVAS.md) nella tua area su Mural |
| 16:20 – 17:00 | A coppie: il compagno legge il tuo canvas e prova a spiegarti la tua app. Usa le dieci domande in fondo a [CANVAS.md](CANVAS.md) |
| 17:30 | Pitch da un minuto: la frase, per chi è, le tre funzioni |

Puoi cambiare idea sul dominio fino all'inizio della prossima lezione. Dopo si costruisce.

## Dieci idee

| # | Idea | In una frase |
|---|---|---|
| 1 | Banca del tempo | Un'ora di chitarra in cambio di un'ora di inglese: il saldo è in ore |
| 2 | Gestionale per band | Brani, prove e scalette: chi suona cosa, in quale tonalità |
| 3 | Gioco di ruolo | Campagne, sessioni, personaggi e oggetti: il diario del master |
| 4 | Fantacalcio tra amici | Rose, formazioni e voti: la classifica la calcola il database |
| 5 | Club del libro | Proposte, voti per il prossimo libro e recensioni dopo l'incontro |
| 6 | Repair café | Oggetti da riparare, riparatori volontari, pezzi usati ed esito |
| 7 | Orto condiviso | Parcelle, turni di irrigazione, raccolti e attrezzi in prestito |
| 8 | Segnalazioni di quartiere | Buche e lampioni rotti: segnalazioni, voti dei vicini, stato |
| 9 | Hackathon | Squadre, progetti e voti della giuria, con la classifica finale |
| 10 | Diario del caffè | Caffè, torrefazioni, metodi e note di gusto: il tuo profilo ideale |

Una tua idea va bene se rispetta i requisiti qui sotto.

## I requisiti minimi

- Gli utenti fanno il **login**: ci sarà una tabella `utenti`. È già nel [modello](schema-modello.sql).
- Almeno **tre «cose»** da ricordare oltre agli utenti (riquadro 6 del canvas): diventeranno tre tabelle.
- Almeno una cosa che **appartiene** a un'altra: un ordine appartiene a un cliente (uno a molti).
- Almeno una relazione **molti a molti**: una persona sa fare tante cose, e una cosa la sanno fare tante persone.
- **Tre funzioni** indispensabili, non di più. Il resto è «se avanza tempo».

## Più avanti: il tuo repository

Questo lo facciamo insieme quando arriviamo alle tabelle. Per ora non serve.

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
