import { Header, Pergamena, ListaLuoghi, Footer } from "./components/index";

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-900 p-8 text-slate-100">
      <Header />
      <Pergamena />
      <ListaLuoghi />
      <Footer />
    </main>
  );
}

// Tappa 1: Stella
