from fastapi import APIRouter
from schemas.employee import EmployeeCreateSchema, EmployeeResponseSchema
from starlette.requests import Request
from starlette.responses import JSONResponse

from depends import get_employee_service


router = APIRouter(prefix="/main", tags=["main"])

@router.get("/hello", 
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


@router.post("/add", 
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



@router.get("/users")
def get_users()-> JSONResponse:
    pass


