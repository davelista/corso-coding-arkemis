export default function CardLuogo({nome, descrizione, zona}){
    return(
        <article className="border-2 border-slate-600 my-3 p-4 bg-sky-300/10 ps-7">
            <p className="text-sm text-yellow-500">{zona}</p> 
            <h2 className="text-xl font-bold">{nome}</h2>
            <p className="text-md text-slate-50/40">{descrizione}</p>
        </article>

    )
}