Stesso metodo: scrivete la richiesta, leggete la risposta, trovate il dato. Queste non le controlla verifica.py: le confrontiamo insieme alla fine.
Consiglio: aprite le risposte nel browser e usate Ctrl+F (su Mac Cmd+F) per trovare quello che cercate.

12. Quanti Pokémon esistono in tutto? Basta chiederne uno solo: /pokemon?limit=1
    → Allenate: leggere i dati di una lista

13. Contro quali tipi è super efficace il tipo fuoco? Cercate in /type/fire
    → Allenate: un JSON annidato su più livelli

14. Dove vive Pikachu (habitat) e quanto è facile da catturare (capture_rate)? Non sta in /pokemon/pikachu…
    → Allenate: la stessa cosa divisa in due risorse

15. Come si chiama in italiano la mossa thunderbolt, e quanta potenza ha? Aprite /move/thunderbolt e con Ctrl+F cercate "it"
    → Allenate: trovare l'elemento giusto in una lista

16. Aprite /pokemon?limit=20. Cosa c'è nel campo next? Apritelo: cosa è cambiato nell'indirizzo? E quale Pokémon trovate per primo?
    → Allenate: la paginazione, cioè come un'API vi dà una lista a pezzi

17. Provate /pokemon/Pikachu con la P maiuscola, poi /pokemon/pika. Che codici rispondono? Ve lo aspettavate?
    → Allenate: i codici di stato, e non dare niente per scontato

18. Strumenti per sviluppatori (F12), scheda Rete: aprite /pokemon/mew e guardate la colonna Tempo. Ricaricate la pagina: il tempo cambia? Perché secondo voi?
    → Allenate: misurare una richiesta

19. curl -v https://pokeapi.co/api/v2/pokemon/ditto: quali header manda curl senza che glieli abbiate chiesti? Sono le righe che iniziano con >
    → Allenate: leggere la richiesta, non solo la risposta. Oggi pomeriggio sarete voi a riceverle

Sfida finale: Indovina chi 🎭
Uno di voi pensa a un Pokémon, gli altri devono indovinarlo solo con richieste: tipo, peso, abilità… Vince chi ci arriva con meno richieste.
