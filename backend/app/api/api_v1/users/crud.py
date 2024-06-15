from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user import User
from .schemas import UserCreate, UserUpdate, UserUpdatePartial


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def update_user(
        session: AsyncSession,
        user: User,
        user_update: UserUpdate | UserUpdatePartial,
        partial: bool = False,
) -> User:
    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()
    return user
