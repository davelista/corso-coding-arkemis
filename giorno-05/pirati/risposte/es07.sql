-- Esercizio 7
-- Il bottino totale di ogni nave, solo arrembaggi riusciti, dalla nave più ricca.
--
-- Colonne:      nave, bottino totale
-- Righe attese: 7
-- In ordine:    sì, dalla più ricca
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 7

SELECT n.nome, SUM(a.bottino) AS bottino_totale 
FROM arrembaggi a RIGHT JOIN navi n ON a.nave_id = n.id 
WHERE esito='riuscito' 
GROUP BY n.nome 
ORDER BY bottino_totale DESC;