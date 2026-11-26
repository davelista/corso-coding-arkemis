import {
  Header,
  Pergamena,
  CardLuogo,
  ListaLuoghi,
  Footer,
} from "./components";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-900 p-8 text-slate-100">
      <div className="mx-auto max-w-5xl">
      <Header />
      <Pergamena>
        <p>
          Stanotte l'ombra di Peter è scappata. Campanellino ha segnato sei
          luoghi: cerchiamola!
        </p>
      </Pergamena>
      <ListaLuoghi />
      <Footer />
      </div>
    </main>
  );
}
