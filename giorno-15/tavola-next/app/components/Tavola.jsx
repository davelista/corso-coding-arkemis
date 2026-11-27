"use client"
import { useEffect, useState } from "react"
import { CardOspite } from ".";


const API = "http://localhost:8000";

export default function Tavola() {

    const [ospiti, setOspiti] = useState([]);
    const [scopri, setScopri] = useState(false)
    const [caricamento, setCaricamento] = useState(false)
    const [errore, setErrore] = useState(null)

    async function caricaOspiti() {
        setCaricamento(true)
        const risposta = await fetch(`${API}/ospiti`)
        try {
            if (risposta.ok) {
                const elenco_ospiti = await risposta.json();
                setOspiti(elenco_ospiti)
            } 
            else {
                setErrore(`A mani vuote: errore ${risposta.status}`) 
            }
        }
        catch {
            setErrore("Il Bianconiglio si è perso")
        }
        setCaricamento(false)
        console.log(ospiti)
    }

    async function invita(id){
        const risposta = await fetch(`${API}/ospiti/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ invitato: true }),
        });
        const ospite = await risposta.json();
        alert(ospite.frase);
        caricaOspiti();
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

    if (caricamento)
        return <p>È tardi, è tardi!…</p>
    if (errore)
        return <p>{errore}</p>

    const aTavola = ospiti.filter((ospite) => ospite.invitato).length

    return (
        <>
            <p>La tavola dei matti è composta da {ospiti.length} ospiti</p>

            <button onClick={scopri_ospiti}>
                scopri
            </button>
            <p>A tavolta:{aTavola} su {ospiti.length}</p>
            <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
                {
                    ospiti.map((ospite) => {
                        return(
                            <CardOspite 
                                key={ospite.id} 
                                nome={ospite.nome} 
                                dove={ospite.dove} 
                                specie={ospite.specie} 
                                invitato={ospite.invitato}
                                onInvita={() => invita(ospite.id)}
                                />
                    )
                    })
                }
            </div>
            {aTavola === ospiti.length && <p>…buon non-compleanno!</p>}
        </>
    )
}