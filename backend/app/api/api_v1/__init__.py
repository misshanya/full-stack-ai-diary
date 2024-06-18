from fastapi import APIRouter

from .users.views import router as users_router
from .auth.views import router as auth_router
from .ai.views import router as ai_router

from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    users_router,
)
router.include_router(
    ai_router,
)