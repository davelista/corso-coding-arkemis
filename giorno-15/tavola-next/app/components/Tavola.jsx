"use client"
import { useEffect, useState } from "react"

const API = "http://localhost:8000"

export default function Tavola() {
  const [ospiti, setOspiti] = useState([])
  const [show, setShow] = useState(false)

  async function get_ospiti(params) {
    const res = await fetch(`${API}/ospiti`)
    const elenco_ospiti = await res.json()
    setOspiti(elenco_ospiti)
  }

  function show_ospiti() {
    setShow(true)
  }
  useEffect(() => {
    get_ospiti()
  }, [show])

  return (
    <>
      <div>La tavola dei matti è composta da {ospiti.length} ospiti</div>
      {ospiti.map((ospite) => {
        return(
          <>
          <div className="p">{ospite.nome}</div>
          <div className="p">{ospite.specie}</div>
          <div className="p">{ospite.dove}</div>
          </>
        )
      })}
    </>
  )
}