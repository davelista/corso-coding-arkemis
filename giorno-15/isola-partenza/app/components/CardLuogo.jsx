import Bottone from "./Bottone.jsx";

export default function CardLuogo({
  nome, descrizione, zona = "Isola che non c'è", indizio, esplorato = false,
}) {
  return (
    <article className="rounded-xl border border-slate-700 bg-slate-800 p-6">
      <p className="text-xs uppercase tracking-widest text-amber-300">{zona}</p>
      <h2 className="mt-2 text-xl font-bold">{nome}</h2>
      <p className="mt-1 text-slate-300">{descrizione}</p>
      <Bottone
        messaggio={indizio}
        disabled={esplorato}
        variante={esplorato ? "secondario" : "primario"}
      >
        {esplorato ? "Già esplorato" : "Cerca qui"}
      </Bottone>
    </article>
  );
}
