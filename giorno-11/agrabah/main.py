"""LA LAMPADA DI AGRABAH · le quattro porte della città.

Avvio (dalla cartella agrabah, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs
Test di un livello (in un secondo terminale):
    pytest -v -k livello_0

Qui c'è solo l'app. Gli import, gli stampi e le rotte li scrivete voi: le consegne sono nel README.
"""

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import get_db
from modelli import TesoroDB, PadroneDB, DesiderioDB
from sicurezza import calcola_hash, controlla_chiave, crea_token, padrone_corrente, password_giusta

# Modelli
class TesoroNuovo(BaseModel):                      
    nome: str = Field(min_length=1)
    valore: int = Field(ge=0)
    maledetto: bool = Field(default=False)

class Tesoro(TesoroNuovo):                         
    model_config = ConfigDict(from_attributes=True)
    id: int

class PadroneNuovo(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    nome: str = Field(min_length=1)
    password: str = Field(min_length=8)

class Padrone(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    nome: str

class DesiderioNuovo(BaseModel):
    testo: str = Field(min_length=3)

class Desiderio(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    testo: str
    esaudito: bool

class Credenziali(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

app = FastAPI(title="La lampada di Agrabah")

@app.get("/")
def read_city() -> dict:
    return {"citta": "Agrabah"}

@app.get("/tesori")
def lista_tesori(valore_min: int | None = None, maledetto: bool | None = None, db: Session = Depends(get_db)) -> list[Tesoro]:
    query = select(TesoroDB).order_by(TesoroDB.id)
    if valore_min is not None:
        query = query.where(TesoroDB.valore >= valore_min)
    if maledetto is not None:
        query = query.where(TesoroDB.maledetto == maledetto)
    tesori = db.scalars(query).all()
    return tesori


@app.get("/tesori/{tesoro_id}")
def leggi_tesoro(tesoro_id: int, db: Session = Depends(get_db)) -> Tesoro:
    tesoro = db.get(TesoroDB, tesoro_id)
    if not tesoro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tesoro non trovato")
    return tesoro

@app.post("/tesori", status_code=status.HTTP_201_CREATED)
def crea_tesoro(tesoro_nuovo: TesoroNuovo, db: Session = Depends(get_db), chiave: None = Depends(controlla_chiave)) -> Tesoro:
    nuovo_tesoro = TesoroDB(**tesoro_nuovo.model_dump())
    db.add(nuovo_tesoro)
    db.commit()
    db.refresh(nuovo_tesoro)
    return nuovo_tesoro

@app.put("/tesori/{tesoro_id}")
def aggiorna_tesoro(tesoro_id: int, tesoro_nuovo: TesoroNuovo, db: Session = Depends(get_db), chiave: None = Depends(controlla_chiave)) -> Tesoro:
    tesoro = db.get(TesoroDB, tesoro_id)
    if not tesoro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tesoro non trovato")
    # for campo, valore in tesoro_nuovo.model_dump().items(): setattr(tesoro, campo, valore)
    tesoro.nome = tesoro_nuovo.nome
    tesoro.valore = tesoro_nuovo.valore
    tesoro.maledetto = tesoro_nuovo.maledetto
    db.commit()
    db.refresh(tesoro)
    return tesoro

@app.delete("/tesori/{tesoro_id}", status_code=status.HTTP_204_NO_CONTENT)
def elimina_tesoro(tesoro_id: int, db: Session = Depends(get_db), chiave: None = Depends(controlla_chiave)) -> None:
    tesoro = db.get(TesoroDB, tesoro_id)
    if not tesoro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tesoro non trovato")
    db.delete(tesoro)
    db.commit()

@app.post("/padroni", status_code=status.HTTP_201_CREATED)
def registra_padrone(padrone_in: PadroneNuovo, db: Session = Depends(get_db)) -> Padrone:
    nuovo_padrone = PadroneDB(username=padrone_in.username, nome=padrone_in.nome, password_hash=calcola_hash(padrone_in.password))
    db.add(nuovo_padrone)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username già preso") 
    db.refresh(nuovo_padrone)
    return nuovo_padrone

@app.post("/login")
def login(credenziali: Credenziali, db: Session = Depends(get_db)) -> Token:
    padrone = db.scalars(select(PadroneDB).where(PadroneDB.username == credenziali.username)).first()
 
    if not padrone or not password_giusta(credenziali.password, padrone.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username o password sbagliati")
        
    token = crea_token(padrone.id)
    return Token(access_token=token)

@app.get("/me")
def chi_sono(padrone: PadroneDB = Depends(padrone_corrente)) -> Padrone:
    return padrone

@app.post("/desideri", status_code=status.HTTP_201_CREATED)
def esprimi_desiderio(desiderio_in: DesiderioNuovo, db: Session = Depends(get_db), padrone: PadroneDB = Depends(padrone_corrente),) -> Desiderio:
    # 1. Regola del Genio: niente parola "desideri" (maiuscola o minuscola)
    if "desideri" in desiderio_in.testo.lower():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Il Genio non può: niente desideri in più",)

    # 2. Controllo limite dei 3 desideri a testa
    miei_desideri = db.scalars(select(DesiderioDB).where(DesiderioDB.padrone_id == padrone.id)).all()
    
    if len(miei_desideri) >= 3:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Hai finito i desideri",)
        
    nuovo_desiderio = DesiderioDB(testo=desiderio_in.testo,padrone_id=padrone.id,)

    db.add(nuovo_desiderio)
    db.commit()
    db.refresh(nuovo_desiderio)
    return nuovo_desiderio

@app.get("/desideri")
def lista_desideri(db: Session = Depends(get_db), padrone: PadroneDB = Depends(padrone_corrente),) -> list[Desiderio]:
    # Solo i desideri del padrone loggato, in ordine di id
    query = (select(DesiderioDB).where(DesiderioDB.padrone_id == padrone.id).order_by(DesiderioDB.id))
    return list(db.scalars(query).all())


@app.delete("/desideri/{desiderio_id}", status_code=status.HTTP_204_NO_CONTENT)
def ritira_desiderio(desiderio_id: int, db: Session = Depends(get_db), padrone: PadroneDB = Depends(padrone_corrente),) -> None:
    # Cerchiamo il desiderio SOLO tra quelli che appartengono a questo padrone
    desiderio = db.scalars(select(DesiderioDB).where(DesiderioDB.id == desiderio_id, DesiderioDB.padrone_id == padrone.id,)).first()
    
    if not desiderio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Desiderio non trovato",)
        
    db.delete(desiderio)
    db.commit()

@app.put("/desideri/{desiderio_id}/esaudito")
def esaudisci_desiderio(desiderio_id: int, db: Session = Depends(get_db), padrone: PadroneDB = Depends(padrone_corrente),) -> Desiderio:
    # 1. Solo chi ha il ruolo "genio" può esaudire i desideri
    if padrone.ruolo != "genio":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Solo il Genio esaudisce",)

    # 2. Il Genio può esaudire il desiderio di chiunque, quindi lo cerchiamo per id
    desiderio = db.get(DesiderioDB, desiderio_id)
    if not desiderio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Desiderio non trovato",)

    # 3. Segniamo il desiderio come esaudito e salviamo
    desiderio.esaudito = True
    db.commit()
    db.refresh(desiderio)
    return desiderio

