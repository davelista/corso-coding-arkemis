const CardOspite = ({ nome, specie, dove, invitato, onInvita}) => {
  let cartellino = invitato ? "A tavola" : "Non invitato"
  return (
    <article className="border border-white-300 p-4 flex flex-col">
      <span>Specie: {specie}</span>
      <h2>Nome: {nome}</h2>
      <p>Dove: {dove}</p>
      <p className="text-red-500">{cartellino}</p>
      {!invitato && <button onClick={onInvita}>Invita</button>}
    </article>
  )
}
export default CardOspite