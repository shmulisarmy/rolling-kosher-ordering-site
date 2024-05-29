from fastapi import APIRouter, Form
from . import database_interface
from fastapi import Request
from fastapi.responses import JSONResponse
import json
from fastapi.templating import Jinja2Templates
from .utils import timeStringToInt

orders_router = APIRouter(tags=["orders"])
templates = Jinja2Templates(directory="orders/templates")
@orders_router.get("/orders/{id}", response_class=JSONResponse)
async def get_order(id: int):
    return database_interface.get_order(id)

@orders_router.get("/create", response_class=JSONResponse)
async def create_order(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@orders_router.post("/create", response_class=JSONResponse)
async def create_order(name: str = Form(...), pickUpTime: str = Form(...), items: str = Form(...)):
    pickUpTimeInt = timeStringToInt(pickUpTime)
    if items[0] == "'" or items[0] == '"':
        items = items[1:-1]
    if items[-1] == "'" or items[-1] == '"':
        items = items[:-1]
    print(f"{name = }, {pickUpTime = }, {pickUpTimeInt = }, {items = }")
    return database_interface.create_order(name, pickUpTime, pickUpTimeInt, items)

@orders_router.put("/orders/{id}", response_class=JSONResponse)
async def update_order(id: int, request: Request):
    return database_interface.update_order(request, id)

@orders_router.delete("/orders/{id}", response_class=JSONResponse)
async def delete_order(id: int):
    database_interface.delete_order(id)
    return JSONResponse({"message": "deleted"}, status_code=200)



@orders_router.get("/all", response_class=JSONResponse)
async def get_all_orders():
    allorders: list[tuple] = database_interface.get_all_orders()
    print(f"{allorders = }")
    allorders: list[list] = [[col for col in order] for order in allorders]
    print(f"{allorders = }")
    for order in allorders:
        order[-1] = json.loads(order[-1])
    return allorders
