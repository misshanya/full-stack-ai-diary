from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .schemas import User, UserCreate, UserUpdate
from . import crud
from .dependencies import get_user_by_id

from core.config import settings

router = APIRouter(
    tags=['Users'],
    prefix=settings.api.v1.users,
)


@router.post('/register/', response_model=User)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud.create_user(session=session, user_in=user_in)


@router.get('/{user_id}/', response_model=User)
async def get_user(
    user: User = Depends(get_user_by_id),
):
    return user


@router.put('/{user_id}/update/')
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(get_user_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )