"use client";

import { useState } from "react";
import Bottone from "./Bottone";

export default function CardLuogo({
  nome,
  descrizione,
  zona = "L'Isola che non c'è",
  indizio,
  esplorato = false
}) {
  const [indizioAperto, setIndizioAperto] = useState(false);

  function apri_indizio() {
    setIndizioAperto(!indizioAperto);
  }

  return (
    <article className="p-5 border-2 border-slate-600 bg-slate-800">
      <p className="text-xs text-yellow-400 uppercase mb-2">
        {zona}
      </p>

      <h2 className="text-xl font-bold mb-2">{nome}</h2>

      <p className="text-slate-400 mb-3">{descrizione}</p>

      {indizioAperto && <p>{indizio}</p>}

      <Bottone
        onClick={apri_indizio}
        disabled={indizioAperto}
      >
        {indizioAperto ? "Indizio aperto" : "Apri indizio"}
      </Bottone>
    </article>
  );
}
