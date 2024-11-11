from fastapi import FastAPI
from app.routers.client import client_router
from app.routers.user import user_router
from app.routers.contract import contract_router


app = FastAPI()

app.include_router(client_router, prefix="/clients", tags=["Clientes"])
app.include_router(user_router, prefix="/users", tags=["Usuários"])
app.include_router(contract_router, prefix="/contracts", tags=["Contratos"])