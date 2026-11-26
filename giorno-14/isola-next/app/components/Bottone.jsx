"use client"

export default function Bottone ({children, messaggio, variante="primario", disabled=false}) {
    return (
        <button className="mt-4 rounded-lg px-4 py-2 font-semibold border-2 bg-amber-700" onClick = {() => alert(messaggio)}>
            Cerca qui!
        </button>
    )
}  