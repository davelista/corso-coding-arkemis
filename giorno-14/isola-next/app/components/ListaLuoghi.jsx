import CardLuogo from "./CardLuogo";
import { luoghi } from "../dati";


export default function ListaLuoghi(){
   return (<>
   {luoghi.map((luogo) => (<CardLuogo key= {luogo.id} nome={luogo.nome} zona={luogo.zona} descrizione={luogo.descrizione} indizio={luogo.indizio} esplorato={luogo.esplorato} />
    ))}</>
    )
}