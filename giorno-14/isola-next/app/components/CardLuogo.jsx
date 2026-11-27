"use client"

import { Children } from "react";
import Bottone from "./Bottone";
import { useState } from "react";

export default function CardLuogo({nome, descrizione, zona="Isola che non c'è", indizio, esplorato = false}) {
    const [aperto, setAperto] = useState(false)
    let scritta = aperto ? "Chiudi indizio" : "Apri indizio"
    
    
    return ( 
        <article className="border-2 border-blue-300/30 bg-blue-900/40 mt-8 pl-8 py-2">
            <h3 className="uppercase text-xs text-amber-400">{zona}</h3>
            <h2 className="text-lg font-bold">{nome}</h2>
            <p className="text-sm text-slate-400 ">{descrizione}</p>
            {aperto && <p className="mt-4 italic text-amber-200">{indizio}</p>}
            <Bottone
                disabled={esplorato}
                onClick={() => setAperto(!aperto)}
                variante={esplorato ? "secondario" : "primario"}
            >
                {scritta}
            </Bottone>
        </article>
    
        
    );
}

