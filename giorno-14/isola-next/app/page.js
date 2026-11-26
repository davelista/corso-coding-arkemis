import Header from "./components/Header"
import Footer from "./components/Footer"
import Pergamena from "./components/Pergamena"; 
import CardLuogo from "./components/CardLuogo";

export default function Home() {
  return (
      <main className="min-h-screen bg-slate-900 p-8 text-slate-100">
        <Header/>
          <Pergamena>
            <p>Stanotte l'ombra di Peter è scappata. Campanellino ha segnato sei luoghi: cerchiamola!</p>
          </Pergamena>
          <CardLuogo zona="LAGUNA" nome="Scoglio del Teschio" descrizione="Una riga che racconta il luogo"/>
          <CardLuogo zona="FORESTA" nome="Tana dei Bimbi Sperduti" descrizione="Una riga che racconta il luogo"/>
          <CardLuogo zona="ISOLA CHE NON C'E'" nome="Laghetto del Coccodrillo" descrizione="Una riga che racconta il luogo"/>
        <Footer/>
      </main>
  );
}
