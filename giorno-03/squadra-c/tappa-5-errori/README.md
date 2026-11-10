# Tappa 5 · Incantesimi andati storti

Non tutto va come previsto: pergamene con voti scritti a parole, un conto da dividere per zero maghi e una Penna Prendiappunti che inventa i numeri.

| Chi | Il tuo file | Il tuo branch | Nella storia |
|---|---|---|---|
| Numero 1 | `leggi_voto.py` | `c-leggi-voto` | La pergamena dei voti |
| Numero 2 | `dividi_conto.py` | `c-dividi-conto` | Il conto da Mielandia |
| Numero 3 | `solo_numeri.py` | `c-solo-numeri` | La Penna Prendiappunti |

## Come si fa

Sempre gli stessi passi. L'esempio è quello del numero 1 della squadra C: al posto del file e del branch mettete i vostri (sono nella tabella qui sopra).

**1. Il branch nuovo, preso dal branch della squadra**

```bash
git switch squadra-c-hogwarts
git pull
git switch -c c-leggi-voto
cd ~/corso-coding-arkemis/giorno-03/squadra-c/tappa-5-errori
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_leggi_voto.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add leggi_voto.py
git commit -m "Tappa 5: leggi_voto"
git push -u origin c-leggi-voto
```

**5. La pull request, verso il branch della squadra**

```bash
gh pr create --base squadra-c-hogwarts --fill
```

Oppure su GitHub: **Compare & pull request**, in alto cambia **base** da `main` a `squadra-c-hogwarts`, poi **Create pull request**.

**6. La review.** Apri la PR del compagno che ti tocca: un commento, **Approve**, poi **Merge pull request**.

## Se ti serve un aiuto

```python
int("7")        # 7
int("sette")    # ValueError: Python si ferma qui

try:
    numero = int(testo)
except ValueError:              # se int() fallisce, si salta qui
    print("Non è un numero")

if persone <= 0:
    raise ValueError("Serve almeno una persona")   # l'errore lo sollevate voi
```

- `except ValueError`, non `except:` da solo: ieri abbiamo visto perché.
- `raise` ferma la funzione, come `return`, ma con un errore.
- Nei test, `with pytest.raises(ValueError):` vuol dire «qui mi aspetto proprio questo errore».
