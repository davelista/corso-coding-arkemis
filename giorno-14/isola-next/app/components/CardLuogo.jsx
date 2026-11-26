export default function CardLuoghi({nome, descrizione, zona="Isola che non c'è"}) {
    return ( 
        <article className="border-2 border-blue-300/30 bg-blue-900/40 mt-8 pl-8 py-2">
            <h3 className="uppercase text-xs text-amber-400">{zona}</h3>
            <h2 className="text-lg font-bold">{nome}</h2>
            <p className="text-sm text-slate-400 ">{descrizione}</p>
        </article>
    
        
    );
}

