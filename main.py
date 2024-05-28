from fastapi import FastAPI, Depends, HTTPException, status, Request, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List, Optional
from fastapi.templating import Jinja2Templates
from orders.routes import  orders_router
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name = 'static')


app.include_router(orders_router, prefix='/orders')


templates = Jinja2Templates(directory='templates')
@app.route('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.route('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})




link = 'http://127.0.0.1:8000'
for route in app.routes[3:]:
    print(f'{link}{route.path }')
#run command: uvicorn main:app --reload