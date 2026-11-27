export default function CardOspite({nome, specie, dove, invitato, onInvita}) {
    return (
        <article className="bg-amber-900 border-2 rounded-md p-8 text-center">
            <p>{specie}</p>
            <h2 className="text-2xl">{nome}</h2>
            <p>{dove}</p>
            <div className="bg-slate-500 border-4 rounded-b-md text">
                {invitato ? "A tavola" : "Non invitato"}
            </div>
            {!invitato && <button onClick={onInvita}>Invita</button>}
        </article>
    )
}