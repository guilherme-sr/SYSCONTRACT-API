from datetime import datetime, timedelta
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from app.schemas import Contract
from app.db.models import ContractModel

class ContractUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def create_contract(self, contract: Contract):
        contract_model = ContractModel(
            client_id = contract.client_id,
            value_hour = contract.value_hour,
            hours_total = contract.hours_total,
            hours_month = contract.hours_month,
            total_value = contract.total_value,
            parcels = contract.parcels,
            value_month = contract.value_month,
            payment_date = contract.payment_date,
            start_date = contract.start_date,
            end_date = contract.end_date,
            auto_renewal = contract.auto_renewal,
            payment_type = contract.payment_type,
            service = contract.service,
            times_week = contract.times_week
        )
        try:
            self.db_session.add(contract_model)
            self.db_session.commit()
        except Exception as e:
            self.db_session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error while creating contract: {str(e)}"
            )
        return contract_model
        
