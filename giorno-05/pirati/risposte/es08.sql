-- Esercizio 8
-- Le navi con almeno due arrembaggi riusciti.
--
-- Colonne:      nave, capitano, quanti riusciti
-- Righe attese: 3
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 8

SELECT n.nome, n.capitano, COUNT(*) AS quanti_riusciti
FROM arrembaggi a RIGHT JOIN navi n ON a.nave_id = n.id
WHERE esito='riuscito'
GROUP BY n.nome, n.capitano
HAVING COUNT(*) >= 2;

-- PROVA COL GRUPPO
SELECT n.nome, n.capitano, COUNT(a.esito) 
FROM navi n LEFT JOIN arrembaggi a ON a.nave_id = n.id
GROUP BY n.nome, n.capitano, a.esito HAVING a.esito='riuscito' AND COUNT(a.esito)>=2;