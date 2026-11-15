# Dal canvas alle rotte: il contratto della tua API

Venerdì avete scritto il canvas: la vostra app in una pagina. Oggi avete visto come parla un'API: un **verbo**, un **percorso**, un **codice di stato**.

Adesso unite le due cose. Prima di scrivere una riga di codice, si scrive il **contratto**: l'elenco delle richieste che la vostra API accetterà. Chi farà il frontend (sempre voi, fra qualche giorno) saprà esattamente cosa chiedere.

## Il metodo, in quattro passi

1. **Riprendete il riquadro 6 del canvas, i dati.** Ogni «cosa» che l'app ricorda diventa una **risorsa**, con un nome al plurale: `libri`, `prove`, `scambi`. Saranno anche le vostre tabelle.
2. **Riprendete il riquadro 7, le azioni.** Ogni azione diventa **una richiesta**. Se legge, è una `GET`. Se crea qualcosa, una `POST`. Se cambia, una `PUT`. Se cancella, una `DELETE`.
3. **Per ogni richiesta, scrivete una riga** della tabella qui sotto.
4. **Riprendete il riquadro 8, chi può fare cosa**, e segnate le richieste che servono **solo a chi ha fatto il login**. Il login arriva fra qualche giorno: per ora basta un sì o un no.

## Cinque regole per i percorsi

| Regola | Sì | No |
|---|---|---|
| I percorsi sono **nomi**, non azioni: l'azione la dice il verbo | `POST /prestiti` | `POST /crea-prestito` |
| Le risorse vanno **al plurale** | `/libri/3` | `/libro/3` |
| L'**id** nel percorso indica **una** cosa | `GET /libri/3` | `GET /libri?id=3` |
| I **filtri** vanno dopo il `?` | `GET /libri?autore=Calvino` | `GET /libri/autore/Calvino` |
| Minuscole, parole unite con il trattino | `/ore-scambiate` | `/OreScambiate` |

## Un esempio: la Banca del tempo

| Azione (riquadro 7) | Verbo | Percorso | Cosa mando | Cosa ricevo | Codici | Login? |
|---|---|---|---|---|---|---|
| Vedo cosa sanno fare gli altri | `GET` | `/competenze` | niente (filtro: `?cerca=chitarra`) | la lista delle competenze | 200 | no |
| Vedo una competenza | `GET` | `/competenze/{id}` | niente | la competenza | 200, 404 | no |
| Pubblico cosa so fare | `POST` | `/competenze` | titolo, descrizione | la competenza con l'id | 201, 422 | sì |
| Chiedo un'ora a qualcuno | `POST` | `/scambi` | competenza_id, ore, data | lo scambio, «in attesa» | 201, 404, 422 | sì |
| Confermo uno scambio | `PUT` | `/scambi/{id}` | stato: «confermato» | lo scambio aggiornato | 200, 404 | sì, solo chi riceve l'ora |
| Tolgo una competenza | `DELETE` | `/competenze/{id}` | niente | niente | 204, 404 | sì, solo il proprietario |
| Vedo il mio saldo | `GET` | `/utenti/{id}/saldo` | niente | le ore date e ricevute | 200, 404 | sì |

## Tocca a voi

Copiate la tabella vuota nel vostro canvas su Mural, oppure in un file `ROTTE.md` nel repo del vostro progetto.

| Azione (riquadro 7) | Verbo | Percorso | Cosa mando | Cosa ricevo | Codici | Login? |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Quante righe?** Da 5 a 10. Meno di 5: l'app fa troppo poco, o mancano delle azioni. Più di 10: state facendo troppo, tornate al riquadro 4 e tagliate gli «se avanza tempo».

## Prima di chiudere: tre domande a un compagno

Scambiatevi la tabella con chi vi sta accanto. Lui risponde sì, no o «non so»:

1. Per ogni funzione del riquadro 4 c'è almeno una richiesta?
2. Ogni percorso è un nome al plurale, e l'azione la dice il verbo?
3. Guardando solo la tabella, saprei cosa mandare e cosa aspettarmi indietro?
