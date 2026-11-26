import { CardLuogo } from "./index";
import { luoghi } from "../dati";

export default function ListaLuoghi() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-4 border-solid-700  ">
      {luoghi.map((luogo) => (
        <CardLuogo
          key={luogo.id}
          descrizione={luogo.descrizione}
          nome={luogo.nome}
          zona={luogo.zona}
        />
      ))}
    </div>
  );
}
