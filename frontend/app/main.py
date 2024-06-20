from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/dnevnik/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/", response_class=HTMLResponse)
async def front_register(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})

@app.get("/login/", response_class=HTMLResponse)
async def front_register(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
