import uvicorn

from api import router as api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI()
app.include_router(
    api_router,
)


origins = [
    "http://localhost",
    "http://localhost:8001",
    "http://127.0.0.1:8001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )