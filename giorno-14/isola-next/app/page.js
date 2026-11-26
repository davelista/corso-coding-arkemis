import Image from "next/image";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Pergamena from "./components/Pergamena";
import CardLuogo from "./components/CardLuogo";
import ListaLuoghi from "./components/ListaLuoghi";
import Bottone from "./components/Bottone";
import Finale from "./components/Finale";

export default function Home() {
  const ritrovata = false;
  return (
    <main className="min-h-screen bg-slate-900 p-8 text-slate-100">
      <div className="mx-auto max-w-5xl">
        <Header />
        <Pergamena>
          Stanotte l'ombra di Peter è scappata. Campanellino ha segnato sei
          luoghi:cerchiamola!
        </Pergamena>
        <ListaLuoghi />
        {ritrovata && <Finale luogo="Londra" />}
        <Footer />
      </div>
    </main>
  );
}
