# Corso intensivo di coding · Arkemis

Il repository del corso. Ogni giorno compare una cartella nuova: `giorno-01`, `giorno-02`, …

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
