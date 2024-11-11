from datetime import datetime, timedelta
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from jose import jwt, JWTError
from decouple import config
from app.db.models import ClientModel
from app.schemas import Client



class ClientUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session


    def create_client(self, client: Client):
        client_model = ClientModel(
            name = client.name,
            email = client.email,
            phone = client.phone,
            birth= client.birth,
            school= client.school,
            serie= client.serie,
            sex= client.sex,
            street= client.street,
            addr_number= client.addr_number,
            addr_comp= client.addr_comp,
            addr_city= client.addr_city,
            addr_region= client.addr_region,
            zip_code= client.zip_code,
            resp_name= client.resp_name,
            resp_cpf= client.resp_cpf,
            resp_rg= client.resp_rg,
            resp_email= client.resp_email,
            resp_phone= client.resp_phone,
            resp_birth= client.resp_birth,
            resp_prof= client.resp_prof,
            resp_sex= client.resp_sex,
        )
        try:
            self.db_session.add(client_model)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Client e-mail already exists'
            )


    def update_client(self, client: Client):
        client_on_db = self.db_session.query(ClientModel).filter_by(email=client.email).first()
        if client_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Client not found'
            )
            client_on_db.name = client.name
            client_on_db.email = client.email
            client_on_db.phone = client.phone
            client_on_db.birth = client.birth
            client_on_db.school = client.school
            client_on_db.serie = client.serie
            client_on_db.sex = client.sex
            client_on_db.street = client.street
            client_on_db.addr_number = client.addr_number
            client_on_db.addr_comp = client.addr_comp
            client_on_db.addr_city = client.addr_city
            client_on_db.addr_region = client.addr_region
            client_on_db.zip_code = client.zip_code
            client_on_db.resp_name = client.resp_name
            client_on_db.resp_cpf = client.resp_cpf
            client_on_db.resp_rg = client.resp_rg
            client_on_db.resp_email = client.resp_email
            client_on_db.resp_phone = client.resp_phone
            client_on_db.resp_birth = client.resp_birth
            client_on_db.resp_prof = client.resp_prof
            client_on_db.resp_sex = client.resp_sex
            self.db_session.commit()
            return client_on_db
