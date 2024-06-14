from fastapi import APIRouter

from core.config import settings

router = APIRouter(
    tags=['Users'],
    prefix=settings.api.v1.users,
)
