import CardLuogo from "./CardLuogo";
import { luoghi } from "../dati";


export default function ListaLuoghi(){
   return (
   <section className="grid grid-cols-1 gap-6 md:grid-cols-3">
   {luoghi.map((luogo) => (
    <CardLuogo 
    key={luogo.id} 
    nome={luogo.nome} 
    zona={luogo.zona} 
    descrizione={luogo.descrizione} 
    indizio={luogo.indizio} 
    esplorato={luogo.esplorato} 
    />
    ))}
    </section>
    );
}