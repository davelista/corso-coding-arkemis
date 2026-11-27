"use client"
import { useState } from "react";
import { Bottone } from ".";

export default function PolvereDiFata() {

    const [numPizzichi, setNumPizzichi] = useState(0);

    function aggiungi_pizzico() {
        setNumPizzichi(numPizzichi + 1)
        console.log(numPizzichi + 1)
    }
    function reset_pizzichi() {
        setNumPizzichi(0)
    }

    return (

        <section className="p-5 border-2 border-slate-600 bg-slate-800 text-center mb-4">
            {
                numPizzichi >= 3 ?
                    <p>Si vola!</p> :
                    <p className="mb-3">Pizzichi di polvere di fata: {numPizzichi} pizzichi</p>

            }
            {
                numPizzichi >= 3 ?
                    <Bottone onClick={reset_pizzichi}>
                        ricomincia
                    </Bottone> :
                    <Bottone onClick={aggiungi_pizzico} >
                        Aggiungi un pizzico
                    </Bottone>
            }
        </section>
    )
}