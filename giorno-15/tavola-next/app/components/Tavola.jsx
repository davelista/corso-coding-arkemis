"use client"
import { useEffect, useState } from "react"
import { CardOspite } from "..";

const API = "http://localhost:8000"

export default function Tavola() {
    const [ospiti, setOspiti] = useState([]);
    const [scopri, setScopri] = useState(false)
    const [caricamento, setCaricamento] = useState(false)
    const [errore, setErrore] = useState(null)

    async function caricaOspiti() {
        setCaricamento(true)
        try{
            const risposta = await fetch(`${API}/ospiti`);
            if(risposta.ok)
            {
                const elencoOspiti = await risposta.json()
                setOspiti(elencoOspiti)
            }
            else{
                setErrore(`A mani vuote: errore ${risposta.status}`)
            }            
        }
        catch {
            setErrore("Il Bianconiglio si è perso")
        }
        setCaricamento(false)
        
    }

    async function invita(id) {
        const risposta = await fetch(`${API}/ospiti/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({ invitato: true}),
        });
        const ospite = await risposta.json()
        alert(ospite.frase)
        caricaOspiti()
    }

    function scopriOspiti() {
        setScopri(!scopri)
    }

    useEffect(() => {
        if(scopri){
            caricaOspiti();
        }
        
    }, [scopri])

    const aTavola = ospiti.filter((ospite) => ospite.invitato).length

    return (
        <>
            <button className="border-2 border-amber-500 " onClick={scopriOspiti}>{scopri ? "Chiudi" : "Scopri"}</button>
            {caricamento && <p>E' tardi, è tardi!</p>}
            {errore && <p>{errore}</p>}
            <p>A tavola: {aTavola} su {ospiti.length}</p>
            {scopri && ospiti.map((ospite) => (               
                <div key={ospite.id} className="grid grid-cols-1 gap-6 md:grid-cols-3">
                    <CardOspite 
                        key={ospite.id}
                        nome={ospite.nome} 
                        dove={ospite.dove} 
                        invitato={ospite.invitato} 
                        specie={ospite.specie} 
                        onInvita={() => invita(ospite.id)}
                    />
                </div>
            ))}

            {aTavola === ospiti.length && <p>...buon non-compleanno!</p>}
        </>
    )

}