"use client"
import { useState } from "react";

export default function PolvereDiFata(){
    
    const [num_pizzichi, setNumPizzichi] = useState(0);

    function aggiungi_pizzico(){
        setNumPizzichi(num_pizzichi + 1)
        console.log(num_pizzichi)
    }

    return(

        <section className="p-5 border-2 border-slate-600 bg-slate-800 text-center mb-4">
            <p className="mb-3">Pizzichi di polvere di fata: {num_pizzichi} pizzichi</p>
            <button type="button"  onClick={aggiungi_pizzico} className="bg-yellow-300 text-slate-900 rounded-full font-bold p-2">
                Aggiungi un pizzico
            </button>
        </section>
    )
}