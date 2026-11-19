# Corso intensivo di coding · Arkemis

Il repository del corso. Ogni giorno compare una cartella nuova: `giorno-01`, `giorno-02`, …

## Le slide e le domande

- **Slide**: tutte nella cartella su Google Drive, giorno per giorno → [Slide del corso](https://drive.google.com/drive/folders/1l-TcKmwASVP2rdnZeEg1761rJiF4JOqm?usp=sharing). Il link è sempre lo stesso: le slide nuove arrivano lì. Il PDF si scarica da File → Scarica → PDF.
- **Domande**: nel forum su Discord, indicando giorno e slide (es. «Giorno 04, slide 12»). La risposta resta per tutti.

## Le giornate

| Giorno | Argomento | Cartella |
|---|---|---|
| 1 | Si parte: Git e setup del computer | [giorno-01](giorno-01) |
| 2 | Codice pulito | [giorno-02](giorno-02) |
| 3 | Python e Git | [giorno-03](giorno-03) |
| 4 | Debugger, errori e SQL | [giorno-04](giorno-04) |
| 5 | Pirati, giallo SQL e progetto | [giorno-05](giorno-05) |
| 6 | HTTP e la prima API | [giorno-06](giorno-06) |
| 7 | Oggetti, il colpo e il database | [giorno-07](giorno-07) |
| 8 | Il colpo passo per passo, la banda e il database | [giorno-08](giorno-08) |
| 9 | SQLAlchemy e il biglietto d'oro | [giorno-09](giorno-09) |
| 10 | Chiave e biglietto | [giorno-10](giorno-10) |

## La prima volta

```bash
gh repo clone davelista/corso-coding-arkemis
cd corso-coding-arkemis
code .
```

Prima, accettate l'invito come collaboratori: arriva per email o su github.com/notifications.
Senza, il push viene rifiutato.

## Ogni mattina

```bash
git switch main
git pull
```

## Come si lavora

- `main` è protetto: nessuno ci scrive direttamente.
- Si lavora su un branch (il vostro nome, la vostra squadra, la vostra coppia), poi si apre una pull request.
- Ogni pull request va letta e approvata da un compagno; il merge lo fa il docente.
- Il repository è pubblico: niente password, token o dati personali nei commit.

## Il setup

Checklist per Mac, Linux e Windows (WSL) e la verifica finale `check_setup.py`: cartella [giorno-01/setup](giorno-01/setup).
Piano B se il setup si blocca: Codespaces, vedi `giorno-01/setup/CODESPACES.md`.
