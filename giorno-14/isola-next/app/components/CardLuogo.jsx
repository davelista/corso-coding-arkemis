import { Bottone } from ".";

export default function CardLuogo({
  nome,
  descrizione,
  zona = "L' Isola che non c'è",
  indizio
}) {
  return (
    <article className="p-5 border-2 border-slate-600 bg-slate-800">
      <p className="text-xs text-yellow-400 uppercase mb-2">{zona}</p>
      <h2 className="text-xl font-bold mb-2">{nome}</h2>
      <p className="text-slate-400 mb-3">{descrizione}</p>
      <Bottone messaggio={indizio} variante="primario">
        <p>Cerca qui</p>
      </Bottone>
    </article>
  );
}