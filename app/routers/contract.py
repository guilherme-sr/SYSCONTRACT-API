from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.depends import get_db_session, token_verifier
from app.schemas import Contract, ContractCreated
from typing import List
from app.db.models import ContractModel
from app.contracts import ContractUseCases

contract_router = APIRouter(prefix='/contract ', dependencies=[Depends(token_verifier)])

@contract_router.post('/', tags=["Contratos"])
def create_contract(contract_data: Contract, db_session: Session = Depends(get_db_session)):
    cc = ContractUseCases(db_session)
    cc.create_contract(contract_data)
    return JSONResponse(
        status_code=201,
        content={"detail": "Contract created successfully"}
    )

@contract_router.get("/", response_model=List[Contract], tags=["Contratos"])
def get_contracts(db_session: Session = Depends(get_db_session)):
    contracts = db_session.query(ContractModel).all()
    return [Contract.from_orm(contract) for contract in contracts]


@contract_router.get("/{contract_id}", response_model=Contract, tags=["Contratos"])
def get_contract_by_id(client_id: int, db_session: Session = Depends(get_db_session)):
    contract = db_session.query(ContractModel).filter(ContractModel.id == contract_id).first()
    if contract is None:
            raise HTTPException(status_code=404, detail="Contract not found")
    return Contract.from_orm(contract)


@contract_router.put("/{contract_id}", response_model=ContractCreated, tags=["Contratos"])
def update_contract(contract_id: int, contract_data: ContractCreated, db_session: Session = Depends(get_db_session)):
    contract = db_session.query(ContractModel).filter(ContractModel.id == contract_id).first()

    if contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")

    for key, value in contract_data.dict(exclude_unset=True).items():
        setattr(contract, key, value)

    db_session.commit() 
    return Contract.from_orm(contract)



@contract_router.delete("/{contract_id}", response_model=Contract, tags=["Contratos"])
def delete_contract(contract_id: int, db_session: Session = Depends(get_db_session)):
    contract = db_session.query(ContractModel).filter(ContractModel.id == contract_id).first()
    if contract is None:
        raise HTTPException(status_code=404, detail="Contract not found")
    db_session.delete(contract)
    db_session.commit()
    return JSONResponse(
        content={'detail': 'Success'},
        status_code=status.HTTP_200_OK
    )
