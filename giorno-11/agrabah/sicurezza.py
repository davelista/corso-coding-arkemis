"""La sicurezza di Agrabah. QUESTO FILE È VUOTO: lo scrivete voi, import compresi.

Cosa ci va, livello per livello:

    Livello 2   CHIAVE_CAVERNA, letta dal file .env
                controlla_chiave        il controllore dell'header X-API-Key

    Livello 3   calcola_hash            dalla password, l'impronta
                password_giusta         la password è quella dell'impronta?

    Livello 4   SECRET_KEY, letta dal file .env
                crea_token              il token JWT: sub e exp
                padrone_corrente        dal token al padrone, con Depends

I nomi contano: i test e main.py cercano proprio questi.
Le avete già scritte tutte venerdì, con altri nomi: riaprite giorno-10 (la tabella è nel README).
"""
