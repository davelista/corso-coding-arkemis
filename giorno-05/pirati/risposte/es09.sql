-- Esercizio 9
-- La nave dell'arrembaggio più ricco di tutti.
--
-- Colonne:      nave, capitano, bottino
-- Righe attese: 1
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 9

SELECT n.nome, n.capitano, MAX(a.bottino) AS bottino
FROM arrembaggi a RIGHT JOIN navi n ON a.nave_id = n.id
WHERE esito='riuscito'
GROUP BY n.nome, n.capitano
ORDER BY bottino DESC
LIMIT 1;

-- PROVA COL GRUPPO 
 SELECT n.nome, n.capitano, MAX(a.bottino)
FROM navi n LEFT JOIN arrembaggi a ON  a.nave_id = n.id
GROUP BY n.nome, n.capitano, a.bottino, a.esito HAVING a.esito='riuscito'
ORDER BY a.bottino DESC 
LIMIT 1;