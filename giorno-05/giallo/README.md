# Il vagone fantasma della Linea Menta

*Un giallo da risolvere con SQL.*

Milano, martedì 13 ottobre 2026. L'ultimo treno della Linea Menta parte da **Porta Codice** alle 23:52 con quattro vagoni e arriva a **Piazza Query** alle 23:58 con tre.

Il terzo vagone è sparito.

La mattina dopo lo ritrovano a **Vecchia Fiera**, una stazione chiusa da vent'anni, con le luci accese e un solo passeggero che dorme beato: lo chef stellato Ottavio Brambilla. La sua valigetta con il quaderno delle ricette, trent'anni di lavoro, non c'è più.

Per la centrale è «un'anomalia tecnica». Il commissario Mapelli non ci crede, ma ha finito i caffè e ha chiesto aiuto a voi.

## Come si inizia

Dalla cartella `giallo/`:

```bash
createdb giallo
psql -d giallo -f giallo.sql
psql -d giallo
```

Dentro psql:

| Comando | Cosa fa |
|---|---|
| `\dt` | Elenca le tabelle |
| `\d persone` | Mostra le colonne di una tabella e i suoi collegamenti |
| `\x auto` | Va a capo quando le righe sono troppo lunghe (utile per leggere i testi) |
| `\q` | Esce |

## Il primo indizio

Tutto parte dal **verbale della polizia** del 13 ottobre 2026 sulla Linea Menta. È nella tabella `verbali`.

## Le regole

- Si lavora **in coppia**: uno scrive le query, l'altro guida. Ogni 15 minuti ci si scambia.
- **Niente AI e niente ricerche online**: si risolve con SQL e ragionamento.
- Ogni indizio va sulla vostra **bacheca su Mural**: un post-it con l'indizio, la query che l'ha trovato e il risultato.
- Il file `giallo.sql` è sigillato: aprirlo non serve. Le risposte stanno nel database.

## Quando pensate di averlo trovato

```sql
SELECT verifica('Nome Cognome');
```

Se è giusto, il commissario vi dice cosa fare dopo. Per la parte extra c'è anche:

```sql
SELECT verifica_mandante('Nome Cognome');
```

## Se vi bloccate

Nella cartella `aiuti/` ci sono tre aiuti, dal più leggero al più esplicito. Apriteli **uno alla volta** e solo dopo averci provato davvero: ogni aiuto aperto va segnato sulla bacheca.
