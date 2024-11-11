from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.depends import get_db_session, token_verifier
from app.clients import ClientUseCases
from app.schemas import Client, ClientSimple, ClientCreated
from typing import List
from app.db.models import ClientModel


client_router = APIRouter(prefix='/client ', dependencies=[Depends(token_verifier)])

@client_router.post('/', tags=["Clientes"])
def create_client(client: Client, db_session: Session = Depends(get_db_session)):
    cc = ClientUseCases(db_session=db_session)
    cc.create_client(client=client)
    return JSONResponse(
        content={'detail': 'Success'},
        status_code=status.HTTP_201_CREATED
    )


@client_router.get("/", response_model=List[Client], tags=["Clientes"])
def get_clients(db_session: Session = Depends(get_db_session)):
    clients = db_session.query(ClientModel).all()
    return [Client.from_orm(client) for client in clients]


@client_router.get("/{client_id}", response_model=Client, tags=["Clientes"])
def get_client(client_id: int, db_session: Session = Depends(get_db_session)):
    client = db_session.query(ClientModel).filter(ClientModel.id == client_id).first()
    if client is None:
            raise HTTPException(status_code=404, detail="Client not found")
    return Client.from_orm(client)



@client_router.put("/{client_id}", response_model=ClientCreated, tags=["Clientes"])
def update_client(client_id: int, client_data: ClientCreated, db_session: Session = Depends(get_db_session)):
    client = db_session.query(ClientModel).filter(ClientModel.id == client_id).first()

    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")

    for key, value in client_data.dict(exclude_unset=True).items():
        setattr(client, key, value)

    db_session.commit() 
    return Client.from_orm(client) 



@client_router.delete("/{client_id}", response_model=Client, tags=["Clientes"])
def delete_client(client_id: int, db_session: Session = Depends(get_db_session)):
    client = db_session.query(ClientModel).filter(ClientModel.id == client_id).first()

    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db_session.delete(client)
    db_session.commit() 
    return JSONResponse(
        content={'detail': 'Success'},
        status_code=status.HTTP_200_OK
    )

@client_router.get("/name/{name}", response_model=List[ClientSimple], tags=["Clientes"])
def get_client_by_name(name: str, db_session: Session = Depends(get_db_session)):
    clients = (
    db_session.query(ClientModel)
    .filter(
        ClientModel.name.ilike(f"%{name}%")
    )
    .all()
    )
    if clients is None:
            raise HTTPException(status_code=404, detail="Client not found")
    return [ClientSimple.from_orm(client) for client in clients]