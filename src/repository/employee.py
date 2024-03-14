from typing import List
from database.models.employee import *
from schemas.employee import EmployeeCreateSchema
from sqlalchemy.future import select
from sqlalchemy import and_, func, insert, update, join, delete

class EmployeeRepositoriy:
    base_model = Employee

    def __init__(self, get_db):
        self.get_db = get_db

    def get_all_employee(self) -> List[EmployeeCreateSchema]:
        with self.get_db() as session:
            result = session.scalars(
                select(self.base_model).order_by(self.base_model.id.desc())
            )
            brands = result.all()
            brands = [EmployeeCreateSchema.from_orm(brand) for brand in brands]  # по хорошему это надо в сервисе делать, но lazy-load не позволяет
            session.commit()
        return brands

    def add_new_employee(self, new_emp: EmployeeCreateSchema) -> str:
        res = "creatr"
        with self.get_db() as session:
            result = session.execute(
                select(self.base_model)
                .where(self.base_model.id == new_emp.id)
            )
            client = result.scalars().first()
            # если нет объекта то добавлем 
            if not client:
                result = session.execute(
                    insert(self.base_model)
                    .values(**new_emp.dict())
                    # .returning(*self.base_model.__table__.c)
                )
                res = "create"
            else : 
                res = "cant add."
            session.commit()
        return res
    
    def remove_employee(self, id: int) -> str:
        res = "creatr"
        with self.get_db() as session:
            result = session.execute(
                select(self.base_model)
                .where(self.base_model.id == id)
            )
            client = result.scalars().first()
            # если нет объекта то добавлем 
            if not client:
                result = session.execute(
                    delete(self.base_model)
                    .where(self.base_model.id == id)
                    # .returning(*self.base_model.__table__.c)
                )
                res = "remove"
            else : 
                res = "id is not in table"
            session.commit()
        return res