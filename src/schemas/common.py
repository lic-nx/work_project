from typing import List, Optional

from pydantic import BaseModel, Field


class ResponseSchema(BaseModel):
    """
    Базовая схема для ответов сервера
    """
    ok: Optional[bool] = True
    count: Optional[int] = Field()


class ParseRequestSchema(BaseModel):
    """
    Схема для запросов парсинга
    """
    source: str = Field(max_length=4, default="api")
    parse: List[str] = Field(default=[])
