import uvicorn

from api import router as api_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(
    api_router,
)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )