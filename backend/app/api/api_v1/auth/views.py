from fastapi import APIRouter

from core.config import settings

router = APIRouter(
    tags=['Auth'],
    prefix=settings.api.v1.auth,
)
