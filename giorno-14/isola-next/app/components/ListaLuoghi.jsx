import { CardLuogo } from "./";
import { luoghi } from "../dati";

export default function ListaLuoghi() {
  return (
    <>
      {luoghi.map((luogo) => (
        <CardLuogo
          key={luogo.id}
          zona={luogo.zona}
          nome={luogo.nome}
          descrizione={luogo.descrizione}
        />
      ))}
    </>
  );
}
