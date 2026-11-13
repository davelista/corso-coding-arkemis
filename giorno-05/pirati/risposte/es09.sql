-- Esercizio 9
-- La nave dell'arrembaggio più ricco di tutti.
--
-- Colonne:      nave, capitano, bottino
-- Righe attese: 1
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 9

SELECT n.nome, n.capitano, a.bottino
FROM public.arrembaggi a
JOIN public.navi n ON a.nave_id = n.id
WHERE a.bottino = (SELECT MAX(bottino) FROM public.arrembaggi);