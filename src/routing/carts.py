from fastapi import APIRouter
from schemas.carts import CartsCreateSchema, CartsResponseSchema
from starlette.requests import Request
from starlette.responses import JSONResponse

from depends import *


router = APIRouter(prefix="/carts", tags=["carts info"])

@router.get("/info", 
    responses={400: {"description": "Bad request"}},
    description="Получение всех сотрудников",
    response_model= CartsResponseSchema
)
# информация об определенной карте
async def get_cart(request: Request,id:int)-> JSONResponse: 
    service = get_carts_service()
    response = service.get_carts(id)
    return {
        "ok": True,
        "count": len(response),
        "result": response
    }

