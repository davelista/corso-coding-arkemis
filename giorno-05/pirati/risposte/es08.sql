-- Esercizio 8
-- Le navi con almeno due arrembaggi riusciti.
--
-- Colonne:      nave, capitano, quanti riusciti
-- Righe attese: 3
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 8

SELECT n.nome, n.capitano, COUNT(a.esito)
FROM public.arrembaggi a
JOIN public.navi n ON a.nave_id = n.id
WHERE a.esito = 'riuscito'
GROUP BY n.nome, n.capitano HAVING COUNT(a.esito) >= 2;