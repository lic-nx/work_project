from typing import List
from database.models.carts import *
from schemas.carts import CartsCreateSchema
from sqlalchemy.future import select
from sqlalchemy import and_, func, insert, update, join, delete

class CartsRepositoriy:
    base_model = Carts

    def __init__(self, get_db):
        self.get_db = get_db

    def get_carts(self, id: int) -> List[CartsCreateSchema]:
        with self.get_db() as session:
            result = session.scalars(
                select(self.base_model)
                .where(self.base_model.id == id)
            )
            brands = result.first()
            brands = [CartsCreateSchema.from_orm(brand) for brand in brands]  # по хорошему это надо в сервисе делать, но lazy-load не позволяет
            session.commit()
        return brands

    
    