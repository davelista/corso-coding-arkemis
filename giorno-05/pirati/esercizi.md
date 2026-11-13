# Il diario di bordo dei Caraibi

Port Royal, 1731. La Compagnia delle Indie ha messo le mani sul diario di bordo di tutte le navi dei Caraibi e vuole sapere chi ha fatto cosa. Il diario è un database, e voi siete gli unici che sanno interrogarlo.

Il database `pirati` ha due tabelle:

| Tabella | Cosa c'è dentro |
|---|---|
| `navi` | 9 navi: nome, capitano, bandiera (`pirata`, `Marina`, `Compagnia delle Indie`, `mercantile`), cannoni, porto base. Due navi non tornano mai in porto: il loro porto è vuoto (NULL) |
| `arrembaggi` | 16 arrembaggi: la nave (`nave_id`), il porto, la data, il bottino in dobloni, l'esito (`riuscito`, `fallito`, `in corso`) |

Ogni arrembaggio è di una nave: `arrembaggi.nave_id` è l'`id` della nave. È lo stesso collegamento tra `ordini.cliente_id` e `clienti.id` del negozio.

Ogni esercizio è una domanda. La risposta è una query SQL. Niente AI: scrivete le query a mano.

## Una volta sola: caricate il diario

Dal terminale (su Windows: Ubuntu, WSL):

```bash
cd ~/corso-coding-arkemis/giorno-05/pirati
createdb pirati
psql -d pirati -f pirati.sql
```

Per guardarci dentro: `psql -d pirati`, poi `\dt` e `\d navi`. Oppure dall'estensione PostgreSQL di VS Code, con database `pirati`.

## Come si lavora

1. Aprite il file dell'esercizio nella cartella `risposte/`, per esempio `risposte/es05.sql`. In alto ci sono la domanda, le colonne che servono e quante righe deve dare la risposta.
2. Scrivete la query sotto i commenti. Una query sola, che finisce con il punto e virgola. Salvate.
3. Se volete vedere il risultato prima, provate la query in psql.
4. Controllate dal terminale, nella cartella `pirati`:

```bash
python3 verifica.py 5     # solo l'esercizio 5: vi dice se è giusto e vi mostra cosa ha risposto il database
python3 verifica.py       # tutti e dieci
```

Il programma vi risponde così:

| Simbolo | Vuol dire |
|---|---|
| ✅ | Giusto |
| ❌ | Non ancora: vi dice cosa non torna (righe, colonne, ordine, errore) e vi dà un suggerimento |
| 🟡 | Il risultato è giusto, ma manca qualcosa che l'esercizio chiede (per esempio ORDER BY) |
| ⏭️ | File ancora vuoto |

Il programma legge e basta: non può cambiare né rovinare il database. L'ordine delle colonne non conta, i nomi delle colonne nemmeno.

## Gli esercizi

| # | Domanda | Colonne | Righe |
|---|---|---|---|
| 1 | Le navi pirata, in ordine alfabetico di nome | nome, capitano | 4 |
| 2 | Gli arrembaggi con più di 5000 dobloni, dal più ricco | porto, data, bottino | 5 |
| 3 | Quante navi non hanno un porto base? | un numero solo | 1 |
| 4 | Le navi della Marina con più di 30 cannoni | nome, cannoni | 2 |
| 5 | Per ogni arrembaggio fallito: porto, data, nave e capitano | porto, data, nave, capitano | 4 |
| 6 | Quanti arrembaggi per ogni esito? | esito, quanti | 3 |
| 7 | Il bottino totale di ogni nave, solo arrembaggi riusciti, dalla più ricca | nave, bottino totale | 7 |
| 8 | Le navi con almeno due arrembaggi riusciti | nave, capitano, quanti riusciti | 3 |
| 9 | La nave dell'arrembaggio più ricco di tutti | nave, capitano, bottino | 1 |
| 10 | Le navi che non hanno mai fatto un arrembaggio, senza usare LEFT JOIN | nave, capitano | 2 |

Gli esercizi 1–4 usano SELECT, WHERE e ORDER BY. Il 5 usa JOIN, il 6 GROUP BY, il 7 e l'8 tutti e due (l'8 anche HAVING). Il 9 e il 10 sono per chi vuole una sfida.

## Se qualcosa non va

| Il programma dice | Cosa fare |
|---|---|
| Non trovo psql | Su Windows: lanciatelo dal terminale di Ubuntu (WSL), non da PowerShell |
| PostgreSQL è spento | WSL: `sudo service postgresql start` · Mac: `brew services start postgresql@16` |
| Il database pirati non c'è | Rifate i tre comandi di «Una volta sola» qui sopra |
