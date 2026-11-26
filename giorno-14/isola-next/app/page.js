import Image from "next/image";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Pergamena from "./components/Pergamena";
import CardLuogo from "./components/CardLuogo";

export default function Home() {
  return (
      <main className="min-h-screen bg-slate-900 p-8 text-slate-100">
        <Header />
        <Pergamena>
          Stanotte l'ombra di Peter è scappata. Campanellino ha segnato sei luoghi:cerchiamola!
        </Pergamena>
        <CardLuogo nome="Isola del Teschio" descrizione= "Rocce a picco e grotte nascoste dove l'ombra potrebbe acquattarsi tra le onde." zona="Laguna"/>
        <CardLuogo nome="Tana dei Bimbi Sperduti" descrizione="Un rifugio segreto sotto gli alberi, pieno di passaggi e sussurri notturni." zona="Foresta" />
        <CardLuogo nome="Laghetto del Coccodrillo" descrizione="Acque calme e riflessi insidiosi dove il ticchettio fa sempre scattare l'allerta."/>
        <Footer />
      </main>
    );
}
