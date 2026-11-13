-- Esercizio 3
-- Quante navi non hanno un porto base?
--
-- Colonne:      un numero solo
-- Righe attese: 1
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 3

SELECT COUNT(*)
FROM public.navi
WHERE porto_base IS NULL;