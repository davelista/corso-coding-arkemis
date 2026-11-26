-- Esercizio 8
-- Le navi con almeno due arrembaggi riusciti.
--
-- Colonne:      nave, capitano, quanti riusciti
-- Righe attese: 3
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 8

SELECT na.nome, na.capitano, COUNT(*) AS tot_arrembaggi
FROM arrembaggi ar
JOIN navi na ON ar.nave_id = na.id
WHERE ar.esito = 'riuscito' 
GROUP BY na.nome, na.capitano
HAVING COUNT(*) >= 2; 