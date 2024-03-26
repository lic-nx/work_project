from fastapi import APIRouter
from schemas.employee import *
from starlette.requests import Request
from starlette.responses import JSONResponse

from depends import *


router = APIRouter(prefix="/main", tags=["main"])

@router.get("/take_all_employee", 
    responses={400: {"description": "Bad request"}},
    description="Получение всех сотрудников",
    response_model= EmployeeResponseSchema
)
async def get_all_employee(request: Request,)-> JSONResponse:
    service = get_employee_service()
    response = service.get_all_employee()
    return {
        "ok": True,
        "count": len(response),
        "result": response
    }


@router.post("/add_employee", 
    responses={400: {"description": "Bad request"}},
    description="добавить сотрудника",
)
async def add_employee(request:EmployeeCreateSchema,)-> JSONResponse:
    service = get_employee_service()
    response = service.add_new_employee(request)
    return {
        "ok": True,
        "count": len(response),
        "result": response
    }



# Models
from sqlalchemy import Column, BIGINT, VARCHAR



@router.post("/remove_users",
    responses={400: {"description": "Bad request"}},
    description="удалить пользователя",)
def remove_users(id: int,)-> JSONResponse:
    service = get_employee_service()
    response = service.remove_employee(id)
    return {
        "ok": True,
        "count": len(response),
        "result": response
    }


@router.post("/update_users",
    responses={400: {"description": "Bad request"}},
    description="обновить сотрудника",)
def update_users(request:EmployeeCreateSchema,)-> JSONResponse:
    service = get_employee_service()
    response = service.update_employee(request)
    return {
        "ok": True,
        # "count": len(response),
        "result": request
    }


