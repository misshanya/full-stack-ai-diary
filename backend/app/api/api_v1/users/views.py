from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .schemas import User, UserCreate
from . import crud

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
    user_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    user = await crud.get_user(session=session, user_id=user_id)
    if user is not None:
        return user
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User {user_id} not found!',
    )
