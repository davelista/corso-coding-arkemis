-- Esercizio 10
-- Le navi che non hanno mai fatto un arrembaggio, senza usare LEFT JOIN.
--
-- Colonne:      nave, capitano
-- Righe attese: 2
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 10

SELECT n.nome, n.capitano 
FROM public.navi n
WHERE n.id NOT IN (SELECT nave_id 
FROM public.arrembaggi) 
GROUP BY n.nome, n.capitano;