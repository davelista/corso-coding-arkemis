export default function CardOspite({nome, specie, dove, invitato, onInvita}) {
    return (
        <article>
            <p>{specie}</p>
            <h2>{nome}</h2>
            <p>{dove}</p>
            <div>
                <p>{invitato ? "A tavola" : "Non invitato"}</p>
                {!invitato && <button onClick={onInvita}>Invita</button>}
            </div>
        </article>
    )
}