# Il Pokédex del professor Oak

Biancavilla, laboratorio del professor Oak. Stanotte è saltata la corrente e il Pokédex si è svegliato **vuoto**: non ricorda più niente, nemmeno com'è fatto Pikachu.

Per fortuna il server centrale della Lega Pokémon funziona ancora. Si chiama **PokeAPI** e risponde a chiunque gli faccia la richiesta giusta:

```
https://pokeapi.co/api/v2/
```

Il professore ha lasciato undici domande. Ogni risposta è una **richiesta HTTP**: la scrivete voi, il server risponde, voi leggete la risposta e copiate il dato nel Pokédex.

E nell'ultima riga del registro del laboratorio c'è un indizio inquietante: *«Qualcosa si è mangiato i dati. Un'ombra, in posizione 94.»*

## Tre modi per fare una richiesta

| Strumento | Come | Quando serve |
|---|---|---|
| **Il browser** | Scrivete l'indirizzo nella barra in alto, come per un sito | Per leggere il JSON. Su Chrome mettete la spunta su «Pretty-print» per vederlo ordinato |
| **curl** | `curl https://pokeapi.co/api/v2/pokemon/pikachu` | La stessa richiesta, dal terminale |
| **curl -i** | `curl -i https://pokeapi.co/api/v2/pokemon/pikachu` | Mostra anche il **codice di stato** e gli **header**, prima del corpo |

Il JSON da terminale è tutto su una riga. Per leggerlo meglio:

```bash
curl -s https://pokeapi.co/api/v2/pokemon/pikachu | python3 -m json.tool | less
```

(`less` si chiude con `q`. `-s` vuol dire «silenzioso»: niente barra di avanzamento.)

Anche gli strumenti per sviluppatori del browser vanno bene: **F12** (su Mac **Cmd + Opt + I**), scheda **Rete** (Network), ricaricate la pagina, cliccate la richiesta: vedete codice di stato, header e risposta.

## Come si lavora

1. Leggete la domanda e scrivete la richiesta: quale indirizzo, quali parametri?
2. Fate la richiesta con il browser o con curl.
3. Trovate il dato nella risposta e scrivetelo in `risposte.txt`, dopo il numero della domanda. Per esempio `1: bulbasaur`.
4. Controllate dal terminale, nella cartella `pokedex`:

```bash
python3 verifica.py        # tutte le risposte
python3 verifica.py 5      # solo la 5, con un suggerimento se è sbagliata
```

| Simbolo | Vuol dire |
|---|---|
| ✅ | Giusto: il dato torna nel Pokédex |
| ❌ | Non ancora: vi dà un suggerimento |
| ⏭️ | Risposta ancora vuota |

`verifica.py` non va su internet: controlla e basta. Le richieste le fate voi.

## Le domande

| # | La domanda | Cosa allenate |
|---|---|---|
| 1 | Di che **tipo** è Pikachu? | Il percorso: `/pokemon/{nome}` e il JSON annidato |
| 2 | Come si chiama il Pokémon **numero 133**? | Lo stesso percorso, con un numero al posto del nome |
| 3 | Quanti **chili** pesa Snorlax? Attenti: il server dà il peso in **ettogrammi** | Leggere un dato e capirne l'unità |
| 4 | Qual è l'**abilità nascosta** di Bulbasaur? (quella con `"is_hidden": true`) | Cercare in una lista dentro il JSON |
| 5 | Che **codice di stato** risponde il server a `/pokemon/missingno`? | I codici di stato: `curl -i` o la scheda Rete |
| 6 | E se sbagliate a scrivere il percorso: `/pokemonn/pikachu`, con due n? | Un altro codice della famiglia 4xx |
| 7 | Nella risposta su Pikachu, che valore ha l'header **content-type**? Basta la parte prima del `;` | Gli header: `curl -i` |
| 8 | Chi è il Pokémon in **posizione 151** della lista? Usate `/pokemon?limit=…&offset=…` | I parametri dopo il `?`. Attenzione: `offset` conta da 0 |
| 9 | Da quale Pokémon **si evolve** Pikachu? Nella risposta su Pikachu cercate il link alla sua `species` e seguitelo | Seguire un link: una risposta vi porta alla richiesta dopo |
| 10 | **Il caso finale.** L'ombra è il Pokémon in **posizione 94** della lista. Di che **tipi** è? Scriveteli separati da una virgola | Tutto insieme: query, link, liste |
| 11 | **Extra.** In quanti Pokémon diversi si può **evolvere** Eevee? Dalla sua `species` arrivate alla sua `evolution_chain` | Due link di fila |

## Le regole

- **Niente AI.** Le richieste le scrivete voi: è l'unico modo per capire com'è fatto un indirizzo.
- A squadre: uno scrive le richieste e condivide lo schermo, gli altri leggono il JSON e cercano il dato. Si cambia ogni tre domande.
- Bloccati da più di 10 minuti su una domanda? `python3 verifica.py N` vi dà un suggerimento. Se non basta, si chiede.

## Domanda per chi finisce prima

Provate a **mandare** qualcosa al server invece di chiedere:

```bash
curl -i -X POST https://pokeapi.co/api/v2/pokemon/pikachu
```

Che codice risponde? Che famiglia è? Secondo voi perché? Ne parliamo tutti insieme alla fine.
