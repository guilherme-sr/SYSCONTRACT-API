import re
from pydantic import BaseModel, validator, EmailStr, Field
from typing import Optional


class User(BaseModel):
    username: str
    email: str
    password: str

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Username format invalid')
        return value

class UserCreated(BaseModel):
    username: str
    password: str

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Username format invalid')
        return value

class Client(BaseModel):
    id: Optional[int]
    name: str
    email: str
    phone: str
    birth: str
    school: str
    serie: str
    sex: str
    street: str
    addr_number: str
    addr_comp: str
    addr_city: str
    addr_region: str
    zip_code: str
    resp_name: str
    resp_cpf: str
    resp_rg: str
    resp_email: str
    resp_phone: str
    resp_birth: str
    resp_prof: str
    resp_sex: str

    class Config:
        orm_mode = True

class ClientSimple(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class ClientCreated(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    birth: Optional[str]
    school: Optional[str]
    serie: Optional[str]
    sex: Optional[str]
    street: Optional[str]
    addr_number: Optional[str]
    addr_comp: Optional[str]
    addr_city: Optional[str]
    addr_region: Optional[str]
    zip_code: Optional[str]
    resp_name: Optional[str]
    resp_cpf: Optional[str]
    resp_rg: Optional[str]
    resp_email: Optional[str]
    resp_phone: Optional[str]
    resp_birth: Optional[str]
    resp_prof: Optional[str]
    resp_sex: Optional[str]
    class Config:
        orm_mode = True

class Contract(BaseModel):
    id: Optional[int]
    client_id: int
    value_hour: str
    hours_total: str
    hours_month: str
    total_value: str
    parcels: str
    value_month: str
    payment_date: str
    start_date: str
    end_date: str
    auto_renewal: bool
    payment_type: str
    service: str
    times_week: str
    class Config:
        orm_mode = True

class ContractCreated(BaseModel):
    value_hour: Optional[str]
    hours_total: Optional[str]
    hours_month: Optional[str]
    total_value: Optional[str]
    parcels: Optional[str]
    value_month: Optional[str]
    payment_date: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    auto_renewal: Optional[bool]
    payment_type: Optional[str]
    service: Optional[str]
    times_week: Optional[str]
    class Config:
        orm_mode = True