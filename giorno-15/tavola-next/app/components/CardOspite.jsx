export default function CardOspite({nome, specie, dove, invitato}) {
    return (
        <article className="border-1 mt-5 p-4">
            <p className="text-sm uppercase mb-2">{specie}</p>
            <h2 className="text-xl font-bold mb-2">{nome}</h2>
            <p className="mb-3">{dove}</p>
            <div className="bg-amber-700 border-2 mb-2">
                <p>{invitato ? "A tavola" : "Non invitato"}</p>
            </div>
        </article>
    )
}