"use client"

import {useState} from "react"


export default function PolvereDiFata() {
    const [pizzichi, setPizzichi] = useState(0)
    return(
        <section>
            <p> Polvere di fata: {pizzichi} pizzichi</p>
            <button onClick = {() => setPizzichi(pizzichi+1)}>
                Un pizzico in più
            </button>
        </section>
    )
}