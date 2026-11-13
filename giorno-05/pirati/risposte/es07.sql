-- Esercizio 7
-- Il bottino totale di ogni nave, solo arrembaggi riusciti, dalla nave più ricca.
--
-- Colonne:      nave, bottino totale
-- Righe attese: 7
-- In ordine:    sì, dalla più ricca
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 7

SELECT navi.nome, SUM(arrembaggi.bottino) AS bottino_totale
FROM navi
JOIN arrembaggi
ON arrembaggi.nave_id = navi.id
WHERE arrembaggi.esito='riuscito'
GROUP BY(navi.nome)
ORDER BY bottino_totale DESC;
