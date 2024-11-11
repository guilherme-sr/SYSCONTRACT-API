from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.models import UserModel as User
from app.schemas import UserCreated
from app.depends import get_db_session
from passlib.context import CryptContext
from decouple import config


FIRST_USER = config('FIRST_USER')
FIRST_USER_PASSWORD = config('FIRST_USER_PASSWORD')

crypt_context = CryptContext(schemes=['sha256_crypt'])

def create_initial_user():
    with next(get_db_session()) as db_session:
        user_on_db = db_session.query(User).filter_by(username=FIRST_USER).first()
        if user_on_db is None:
            user_on_db = User(
                username=FIRST_USER,
                email=FIRST_USER,
                password=crypt_context.hash(FIRST_USER_PASSWORD),
            )
            db_session.add(user_on_db)
            db_session.commit()