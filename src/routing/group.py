from fastapi import APIRouter
from schemas.employee import GroupCreateSchema
from starlette.requests import Request
from starlette.responses import JSONResponse
from sqlalchemy import Column, BIGINT, VARCHAR
from depends import *


router = APIRouter(prefix="/group", tags=["group"])

@router.post("/new_group",
    responses={400: {"description": "Bad request"}},
    description="добавить группу",)
async def new_group(request:GroupCreateSchema,)-> JSONResponse:
    service = get_group_service()
    response = service.add_new_group(request)
    return {
        "ok": True,
        "count": len(response),
        "result": response
    }



@router.post("/add_to_group",
    responses={400: {"description": "Bad request"}},
    description="добавить работников в группу",)
async def insert_into_group(request:GroupCreateSchema,)-> JSONResponse:
    # service = get_group_service()
    # response = service.add_new_group(request)
    pass
    return {
        "ok": True,
        "count": len(response),
        "result": response
    }