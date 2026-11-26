"use client"

export default function Bottone({
    children, messaggio, variante = "primanrio", disabled = false
}) {

    const colori =
        variante === "primario"
            ? "bg-yellow-300 text-slate-900 rounded-full font-bold p-2"
            : "border border-slate-500 text-slate-400";

    return (
        <button className={`${colori}`} onClick={() =>
            alert(messaggio)
        }>
            {children}
        </button>
    )
}
