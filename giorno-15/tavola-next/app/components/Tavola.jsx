"use client"
import { useEffect, useState } from "react"
import { CardOspite } from "."

const API = "http://localhost:8000"

export default function Tavola() {
  const [ospiti, setOspiti] = useState([])
  const [show, setShow] = useState(false)
  const [caricamento, setCaricamento] = useState(true)
  const [errore, setErrore] = useState(null)

  async function get_ospiti(params) {
    try {
      const res = await fetch(`${API}/ospiti`)
      if (res.ok) {
        const elenco_ospiti = await res.json()
        setOspiti(elenco_ospiti)
      } else {
        setErrore(`A mani vuote: errore ${res.status}`)
      }
    } catch (errore) {
      setErrore("Il Bianconiglio si è perso")
      setCaricamento(false)
    }
    setCaricamento(false)
  }

  async function invita(id) {
    try {
      const res = await fetch(`${API}/ospiti/${id}`, {
        method: "PUT",
        headers:{"Content-Type": "application/json" },
        body: JSON.stringify({invitato: true})
      })
      if (res.ok) {
        const ospite = await res.json()
        alert(ospite.frase)
        get_ospiti()
      }
    } catch (error) {
      setErrore("Hai sbagliato tutto")
    }
  }

  function show_ospiti() {
    setShow(true)
  }
  useEffect(() => {
    get_ospiti()
  }, [])

  if (caricamento) {
    return(
      <p>«È tardi, è tardi!…»</p>
    )
  }
  if (errore) {
    return(
      <p>{errore}</p>
    )
  }

  const aTavola = ospiti.filter((ospite) => ospite.invitato).length

  return (
    <section>
      <p>«A tavola: {aTavola} su {ospiti.length}»</p>
      <div>La tavola dei matti è composta da {ospiti.length} ospiti</div>
      <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
        {ospiti.map((ospite) => {
          return (
            <CardOspite
              key={ospite.id}
              nome={ospite.nome}
              specie={ospite.specie}
              dove={ospite.specie}
              invitato={ospite.invitato}
              onInvita={() => invita(ospite.id)}
            />
          )
        })}
      </div>
      {aTavola === ospiti.length && <p>…buon non-compleanno!</p>}
    </section>
  )
}