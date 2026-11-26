import Image from "next/image";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Pergamena from "./components/Pergamena";
import CardLuogo from "./components/CardLuogo";
import ListaLuoghi from "./components/ListaLuoghi";

export default function Home() {
  return (
      <main className="min-h-screen bg-slate-900 p-8 text-slate-100">
        <Header />
        <Pergamena>
          Stanotte l'ombra di Peter è scappata. Campanellino ha segnato sei luoghi:cerchiamola!
        </Pergamena>
        <ListaLuoghi/>
      </main>
    );
}
