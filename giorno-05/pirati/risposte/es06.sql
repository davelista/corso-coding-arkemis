-- Esercizio 6
-- Quanti arrembaggi ci sono per ogni esito?
--
-- Colonne:      esito, quanti
-- Righe attese: 3
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 6

SELECT esito, COUNT(*) FROM arrembaggi GROUP BY esito;