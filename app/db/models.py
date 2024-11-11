from sqlalchemy import Column, String, Integer
from app.db.base import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    email = Column('email', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)

class ClientModel(Base):
    __tablename__ = 'clients'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String, nullable=False)
    email = Column('email', String, nullable=False, unique=True)
    phone = Column('phone', String, nullable=False)
    birth = Column('birth', String, nullable=False)
    school = Column('school', String, nullable=False)
    serie = Column('serie', String)
    sex = Column('sex', String, nullable=False)
    street = Column('street', String, nullable=False)
    addr_number = Column('addr_number', String, nullable=False)
    addr_comp = Column('addr_comp', String)
    addr_city = Column('addr_city', String, nullable=False)
    addr_region = Column('addr_region', String, nullable=False)
    zip_code = Column('zip_code', String, nullable=False)
    resp_name = Column('resp_name', String, nullable=False)
    resp_cpf = Column('resp_cpf', String, nullable=False)
    resp_rg = Column('resp_rg', String, nullable=False)
    resp_email = Column('resp_email', String, nullable=False)
    resp_phone = Column('resp_phone', String, nullable=False)
    resp_birth = Column('resp_birth', String)
    resp_prof = Column('resp_prof', String)
    resp_sex = Column('resp_sex', String, nullable=False)

class ContractModel(Base):
    __tablename__ = 'contracts'
    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    client_id = Column('client_id', Integer, nullable=False)
    value_hour = Column('value_hour', String, nullable=False)
    hours_total = Column('hours_total', String, nullable=False)
    hours_month = Column('hours_month', String, nullable=False)
    total_value = Column('total_value', String, nullable=False)
    parcels = Column('parcels', String, nullable=False)
    value_month = Column('value_month', String, nullable=False)
    payment_date = Column('payment_date', String, nullable=False)
    start_date = Column('start_date', String, nullable=False)
    end_date = Column('end_date', String, nullable=False)
    auto_renewal = Column('auto_renewal', String, nullable=False)
    payment_type = Column('payment_type', String, nullable=False)
    service = Column('service', String, nullable=False)
    times_week = Column('times_week', String, nullable=False)
    