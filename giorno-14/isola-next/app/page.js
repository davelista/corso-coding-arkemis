import Header from "./components/Header";
import Footer from "./components/Footer";
import CardLuogo from "./components/CardLuogo";
import Pergamena from "./components/Pergamena";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-900 p-8 text-slate-100">
      <Header />
      <Pergamena/>
      <div className="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-1 gap-4 border-solid-700  ">
        <CardLuogo luogo={{ nome: "Luogo 1", descrizione: "Descrizione del luogo 1" }} />
        <CardLuogo luogo={{ nome: "Luogo 2", descrizione: "Descrizione del luogo 2" }} />
        <CardLuogo luogo={{ nome: "Luogo 3", descrizione: "Descrizione del luogo 3" }} />
      </div>
      <Footer />
    </main>
  );
}
