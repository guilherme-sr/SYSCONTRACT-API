from fastapi import FastAPI
from app.routes import user_router, client_router, contract_router
from app.routers.startup import create_initial_user


app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_initial_user()

@app.get('/', tags=["API"])
def health_check():
    return "Ok"

app.include_router(user_router)
app.include_router(client_router)
app.include_router(contract_router)