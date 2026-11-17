# La banda · da soli

La collana è al sicuro. Adesso Lupin deve tenere in ordine la sua banda: chi entra, chi cambia parte del bottino, chi se ne va. Il registro dei complici è un dizionario, e serve un'API per gestirlo.

Le GET sono già fatte. **POST, PUT e DELETE le scrivete voi, da soli**, ognuno sul suo computer. Avete già tutti gli strumenti: le slide «Scrivere un dizionario» e i livelli 5, 6 e 7 del colpo.

## Prima di tutto

Dalla cartella `giorno-07`, con il venv acceso:

```bash
cd banda
fastapi dev main.py          # poi aprite http://127.0.0.1:8000/docs
```

In un secondo terminale, sempre dentro `banda`: `pytest -v`. Oggi niente branch e niente push: è un allenamento.

## Le tre rotte

| Ordine | Rotta | Risponde | Nel dizionario | Come nel colpo |
|---|---|---|---|---|
| 1 | `POST /complici` | 201 e il complice con l'id | `banda[nuovo_id] = complice` | livello 5 |
| 2 | `PUT /complici/{complice_id}` | 200, oppure 404 `"Complice non trovato"` | `banda[complice_id] = complice` | livello 6 |
| 3 | `DELETE /complici/{complice_id}` | 204, oppure 404 `"Complice non trovato"` | `del banda[complice_id]` | livello 7 |

Un test alla volta: `pytest -v -k post`, poi `-k put`, poi `-k delete`.

<details><summary>Aiutino: la forma di ogni rotta</summary>

```python
@app.<verbo>("<percorso>", status_code=...)       # 201 per la POST, 204 per la DELETE
def nome_funzione(complice_id: int, dati: CompliceNuovo) -> Complice:
    # 1. se serve: il complice c'è? Altrimenti 404 (leggi_complice lo fa già)
    # 2. il lavoro sul dizionario: una riga
    # 3. return (tranne la DELETE)
```

Non tutte le rotte hanno sia `complice_id` sia `dati`: la POST ha solo `dati`, la DELETE solo `complice_id`.

</details>

## Se finite prima

1. `POST` con un nome già nella banda: 409 `"Nome già nella banda"`.
2. `GET /complici?specialita=fuga`: solo i complici con quella specialità.

I test: `pytest -v -k extra`.
