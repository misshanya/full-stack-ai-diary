from sqlalchemy.ext.asyncio import AsyncSession

from auth.utils import hash_password
from core.models.user import User
from .schemas import UserCreate, UserUpdate, UserUpdatePartial


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    user = User(**user_in.model_dump())
    user.password = hash_password(user.password)
    session.add(user)
    await session.commit()
    return user


async def update_user(
        session: AsyncSession,
        user: User,
        user_update: UserUpdate | UserUpdatePartial,
        partial: bool = False,
) -> User:
    if user_update.password:
        user_update.password = hash_password(user_update.password)
        
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user(
        session: AsyncSession,
        user: User,
) -> None:
    await session.delete(user)
    await session.commit()
