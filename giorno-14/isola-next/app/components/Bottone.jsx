"use client";

export default function Bottone({
    children, messaggio, variante = "primario", disabled=false, onClick,
}) {
    const colori = variante === "primario"
    ? "bg-amber-300 text-slate-900"
    : "border border-slate-500 text-slate-400";

    return (
        <button
            type="button"
            disabled={disabled}
            onClick={onClick}
            className={`mt-4 rounded-lg px-4 py-2 font-semibold ${colori}`}
        >
            {children}
        </button>
    )

}