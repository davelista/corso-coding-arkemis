"use client"
import { useEffect, useState } from "react"
import { CardOspite } from "..";

const API = "http://localhost:8000"

export default function Tavola() {
    const [ospiti, setOspiti] = useState([]);
    const [scopri, setScopri] = useState(false)
    async function caricaOspiti() {
        const risposta = await fetch(`${API}/ospiti`);
        const elencoOspiti = await risposta.json()
        setOspiti(elencoOspiti)
    }

    function scopriOspiti() {
        setScopri(!scopri)
    }

    useEffect(() => {
        if(scopri){
            caricaOspiti();
        }

    }, [scopri])

    return (
        <>
            <button className="border-2 border-amber-500 " onClick={scopriOspiti}>{scopri ? "Chiudi" : "Scopri"}</button>
            {scopri && ospiti.map((ospite) => (
            <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
                    <CardOspite
                        key={ospite.id}
                        nome={ospite.nome} 
                        dove={ospite.dove}
                        invitato={ospite.invitato}
                        specie={ospite.specie}
                />
            </div>
            ))}
        </>
    )

}