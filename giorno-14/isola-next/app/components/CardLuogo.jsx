import { Bottone } from "./"

export default function CardLuogo({nome, descrizione, zona, indizio, esplorato = false}){
    return(
        <article className="border-2 border-slate-600 my-3 p-4 bg-sky-300/10 ps-7">
            <p className="text-sm text-yellow-500">{zona}</p> 
            <h2 className="text-xl font-bold">{nome}</h2>
            <p className="text-md text-slate-50/40">{descrizione}</p>
            <Bottone disabled={esplorato} variante={esplorato?"secondario":"primario"} messaggio={indizio} ></Bottone>
        </article>
    )
}