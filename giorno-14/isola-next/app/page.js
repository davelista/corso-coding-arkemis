import {
  Header,
  Pergamena,
  ListaLuoghi,
  Footer,
  Finale,
} from "./components/index";

export default function Home() {
  const ritrovata = true;

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
        {ritrovata && <Finale luogo="Londra" />}
        <Footer />
      </div>
    </main>
  );
}

// Tappa 1: Stella
