import Pergamena from "./Pergamena.jsx";

export default function Finale({ luogo }) {
  return (
    <Pergamena>
      <h2 className="text-2xl font-bold">L'ombra è stata ritrovata!</h2>
      <p className="mt-2">Era a {luogo}, chiusa in un cassetto.
        Wendy l'ha ricucita con ago e filo.</p>
    </Pergamena>
  );
}
