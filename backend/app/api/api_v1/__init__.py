from fastapi import APIRouter

from .users.views import router as users_router

from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    users_router,
)