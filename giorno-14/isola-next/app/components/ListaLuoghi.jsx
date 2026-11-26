import { CardLuogo } from "./";
import { luoghi } from "../dati";

export default function ListaLuoghi() {
  return (
    <section className="grid grid-cols-1 gap-6 md:grid-cols-3">
      {luoghi.map((luogo) => (
        <CardLuogo
          indizio={luogo.indizio}
          key={luogo.id}
          zona={luogo.zona}
          nome={luogo.nome}
          descrizione={luogo.descrizione}
          esplorato={luogo.esplorato}
        />
      ))}
    </section>
  );
}
