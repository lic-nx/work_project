from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel, Field, validator
from schemas.common import ResponseSchema
 # для связи с работниками
class WorkersRequestSchema(BaseModel):
    emploeer_id: str = Field(alias="emploeer_id")
    count: int
    carts_id: str = Field(alias="carts_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ClientsRequestSchema(BaseModel): # для связи с криентами
    clients_id: str = Field(alias="clients_id")
    count: int
    carts_id: str = Field(alias="carts_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class CartsCreateSchema(BaseModel):
    """
    Схема для создания объекта карты.
    Для сопоставления имен полей используются псевдонимы.
    """
    id: int = Field(alias="id")
    # manager:List[WorkersRequestSchema] # должна быть связка с менеджерами
    # responsible:List[WorkersRequestSchema]
    # participants:List[WorkersRequestSchema]
    company:str = Field(alias="company")
    address:str = Field(alias="address")
    file_path:str = Field(alias="file_path")
    delivered:datetime = Field(alias="delivered")
    contract_number:str = Field(alias="contract_number")
    # contacts:List[ClientsRequestSchema]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class CartsResponseSchema(ResponseSchema):
    """
    Схема для ответов сервера
    """
    result: Optional[Union[
        List[CartsCreateSchema], 
        CartsCreateSchema,
    ]] = Field()

