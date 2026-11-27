"use client"

export default function Bottone ({children, messaggio, variante="primario", disabled=false, onClick}) {
    const colore = variante==="primario"?"bg-slate-400 text-white" : "bg-amber-700 text-black"
    return (
        <button 
        disabled={disabled} 
        className={`mt-4 rounded-lg px-4 py-2 font-semibold border-2 ${colore}`} 
        onClick = {onClick}>
            {children}
        </button>
    )
}  