from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.depends import get_db_session, token_verifier
from app.auth_user import UserUseCases
from app.schemas import User, UserCreated

user_router = APIRouter()

@user_router.post('/register', tags=["Usuários"])
def user_register(
    user: User,
    db_session: Session = Depends(get_db_session),
):
    uc = UserUseCases(db_session=db_session)
    uc.user_register(user=user)
    return JSONResponse(
        content={'detail': 'success'},
        status_code=status.HTTP_201_CREATED
    )


@user_router.post('/login', tags=["Usuários"])
def user_register(
    request_form_user: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db_session),
):
    uc = UserUseCases(db_session=db_session)
    user = UserCreated(
        username=request_form_user.username,
        password=request_form_user.password
    )

    auth_data = uc.user_login(user=user)
    return JSONResponse(
        content=auth_data,
        status_code=status.HTTP_200_OK
    )

@user_router.get('/verify_token', tags=["Usuários"])
def user_me(
    access_token: str = Depends(token_verifier)
):
    return JSONResponse(
        content={'detail': 'Success'},
        status_code=status.HTTP_200_OK
    )
