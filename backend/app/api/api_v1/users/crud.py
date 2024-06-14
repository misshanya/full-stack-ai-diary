from sqlalchemy.ext.asyncio import AsyncSession

from core.models.user import User


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)
