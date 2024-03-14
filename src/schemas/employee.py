from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel, Field, validator
from schemas.common import ResponseSchema

class EmployeeCreateSchema(BaseModel):
    """
    Схема для создания объекта сотрудников.
    Для сопоставления имен полей используются псевдонимы.
    """

    # id: Optional[int] = Field(alias="id")
    # name: Optional[str] = Field(alias="name")
    # last_name: Optional[str] = Field(alias="last_name")
    # second_name: Optional[str] = Field(alias="second_name")
    # active: Optional[bool] = Field(alias="active")
    # work_position:Optional[str]  = Field(alias="work_position")
    # last_login:Optional[str]    = Field(alias="last_login")
    # date_register:Optional[str] = Field(alias="date_register")
    # personal_photo:Optional[str] = Field(alias="personal_photo")

    id: int = Field(alias="id")
    full_name: Optional[str] = Field(alias="full_name")
    post: Optional[str] = Field(alias="post")
    personal_phone:Optional[str] = Field(alias= "personal_phone")
    mail:Optional[str] = Field(alias= "mail")
    work_phone:Optional[str] = Field(alias="work_phone")
    internal_phone:Optional[str] = Field(alias="internal_phone")
    telegramm:Optional[str] = Field(alias="telegramm")
    skype:Optional[str] = Field(alias= "skype")
    bitrix24:Optional[str] = Field(alias= "bitrix24")
    division:Optional[str] = Field(alias= "division")
    birthday:Optional[datetime] = Field(alias="birthday")
    personal_photo:Optional[str] = Field(alias="personal_photo")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class EmployeeResponseSchema(ResponseSchema):
    """
    Схема для ответов сервера
    """
    result: Optional[Union[
        List[EmployeeCreateSchema], 
        EmployeeCreateSchema,
    ]] = Field()

