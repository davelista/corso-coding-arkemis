"use client"
import { useEffect, useState } from "react"

const API = "http://localhost:8000";

export default function Tavola() {

    const [ospiti, setOspiti] = useState([]);
    const [scopri, setScopri] = useState(false)

    async function caricaOspiti() {
        const risposta = await fetch(`${API}/ospiti`);
        const elenco_ospiti = await risposta.json();
        setOspiti(elenco_ospiti)
    }

    function scopri_ospiti() {
        setScopri(true);
    }

    //Hook
    useEffect(() => {
        if (scopri) {
            caricaOspiti()
        }
    }, [scopri])

    return (
        <>
            <p>La tavola dei matti è composta da {ospiti.length} ospiti</p>

            <button onClick={scopri_ospiti}>
                scopri
            </button>

            {
                ospiti.map((ospite) => {
                    return (
                        <div key={ospite.id}>
                            <br />
                            <p>{ospite.nome}</p>
                            <p>{ospite.specie}</p>
                            <p>{ospite.dove}</p>
                        </div>
                    )
                })
            }
        </>
    )
}