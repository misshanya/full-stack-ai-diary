from fastapi import APIRouter, Depends

from core.config import settings
from core.models import User

from .validation import validate_auth_user


router = APIRouter(
    tags=['Auth'],
    prefix=settings.api.v1.auth,
)


@router.post('/test-login/')
async def test_login(user: User = Depends(validate_auth_user)):
    return user


@router.post('/login/')
async def login(
    user: User = Depends(validate_auth_user),
):
    pass