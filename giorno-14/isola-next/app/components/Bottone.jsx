"use client"

export default function Bottone({
    children, messaggio, variante = "primario", disabled = false, onClick,
}) {

    const colori =
        variante === "primario"
            ? "bg-yellow-300 text-slate-900 rounded-full font-bold p-2"
            : "border border-slate-500 text-slate-400 rounded-full font-bold p-2";

    return (
        <button className={`${colori}`}
            onClick={onClick}
            disabled={disabled}>
            {children}
        </button>
    )
}
