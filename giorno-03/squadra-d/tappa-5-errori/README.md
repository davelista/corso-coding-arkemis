# Tappa 5 · Incantesimi andati storti

Non tutto va come previsto: pergamene con voti scritti a parole, un conto da dividere per zero maghi e una Penna Prendiappunti che inventa i numeri.

| Chi | Il tuo file | Nella storia |
|---|---|---|
| Numero 1 | `leggi_voto.py` | La pergamena dei voti |
| Numero 2 | `dividi_conto.py` | Il conto da Mielandia |
| Numero 3 | `solo_numeri.py` | La Penna Prendiappunti |

## Come si fa

Sempre gli stessi passi. L'esempio è quello di Anna, numero 1 della squadra D: al posto di `anna` e del file mettete il vostro nome e il vostro file.

**1. Il branch nuovo**

```bash
git switch main
git pull
git switch -c d-anna-t5
cd ~/corso-coding-arkemis/giorno-03/squadra-d/tappa-5-errori
```

**2. Il codice.** Apri il tuo file e leggi la storia in alto. Poi, al posto di `pass`, scrivi il codice: gli esempi dicono cosa deve uscire.

**3. La prova.** `pytest test_leggi_voto.py -v` (con il nome del vostro file). Rosso? Leggi l'ultima riga dell'errore e riprova. Tutto verde? Hai finito.

**4. Il lavoro va su GitHub**

```bash
git add leggi_voto.py
git commit -m "Tappa 5: leggi_voto"
git push -u origin d-anna-t5
```

**5. La pull request.** Su GitHub: **Compare & pull request**, poi **Create pull request**.

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
