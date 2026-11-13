-- Esercizio 9
-- La nave dell'arrembaggio più ricco di tutti.
--
-- Colonne:      nave, capitano, bottino
-- Righe attese: 1
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 9

SELECT navi.nome, navi.capitano, SUM(arrembaggi.bottino) 
FROM navi
JOIN arrembaggi 
ON arrembaggi.nave_id = navi.id
GROUP BY(navi.nome, navi.capitano, arrembaggi.bottino)
ORDER BY arrembaggi.bottino DESC LIMIT 1;
