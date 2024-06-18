from fastapi import Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from starlette import status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .helpers import (
    TOKEN_TYPE_FIELD,
    ACCESS_TOKEN_TYPE,
    REFRESH_TOKEN_TYPE,
)
from auth.utils import (
    decode_jwt,
    validate_password,
)
from api.api_v1.users.schemas import User as UserSchema
from core.models.user import User as UserTable

from core.models import db_helper

invalid_token_http_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token",
        )

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login/",
)


def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
) -> dict:
    try:
        payload = decode_jwt(
            token=token,
        )
    except InvalidTokenError:
        raise invalid_token_http_exception
    return payload


def validate_token_type(
    payload: dict,
    token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise invalid_token_http_exception


def get_user_by_token_sub(
        payload: dict,
        session: AsyncSession = Depends(db_helper.session_getter),
) -> UserSchema:
    user_id: int | None = payload.get("sub")
    user = session.get(UserTable, id=user_id)
    if user:
        return user
    raise invalid_token_http_exception


def get_auth_user_from_token_of_type(token_type: str):
    def get_auth_user_from_token(
        payload: dict = Depends(get_current_token_payload),
    ) -> UserSchema:
        validate_token_type(payload, token_type)
        return get_user_by_token_sub(payload)

    return get_auth_user_from_token


class UserGetterFromToken:
    def __init__(self, token_type: str):
        self.token_type = token_type

    def __call__(
        self,
        payload: dict = Depends(get_current_token_payload),
    ):
        validate_token_type(payload, self.token_type)
        return get_user_by_token_sub(payload)


# get_current_auth_user = UserGetterFromToken(ACCESS_TOKEN_TYPE)
get_current_auth_user = get_auth_user_from_token_of_type(ACCESS_TOKEN_TYPE)

get_current_auth_user_for_refresh = UserGetterFromToken(REFRESH_TOKEN_TYPE)


async def validate_auth_user(
    session: AsyncSession = Depends(db_helper.session_getter),
    username: str = Form(),
    password: str = Form(),
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )
    
    stmt = select(UserTable).where(UserTable.username == username)
    result = await session.execute(stmt)
    user = result.scalars().first()

    if not user:
        raise unauthed_exc
    
    if not validate_password(
        password=password,
        hashed_password=user.password,
    ):
        raise unauthed_exc
    
    return user
