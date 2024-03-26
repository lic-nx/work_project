from typing import List
from database.models.employee import *
from schemas.employee import *
from sqlalchemy.future import select
from sqlalchemy import and_, func, insert, update, join, delete
from sqlalchemy.orm import joinedload

from typing import NamedTuple, Union, List, Dict

class ResponseEmployeGroup(NamedTuple):
    data: Union[Group, List[Group], Dict, List[Dict], None] = None




class EmployeeRepositoriy:
    base_model = Employee
    relationships_group = Group
    test = Employee_Group
    def __init__(self, get_db):
        self.get_db = get_db

    def get_all_employee(self) -> List[EmployeeCreateSchema]:
        with self.get_db() as session:
            result = session.scalars(
                select(self.base_model).options(
                    joinedload(self.base_model.group)
                )
               
                .order_by(self.base_model.id.desc())
            ).unique()
            brands = result.all()
            # brands = [EmployeeCreateSchema.from_orm(brand) for brand in brands]  # по хорошему это надо в сервисе делать, но lazy-load не позволяет
            session.commit()
        return brands

    
    def create_emplouer_group(self, emp_group: GroupCreateSchema):
        with self.get_db() as session:
            result = session.execute(
                select(self.relationships_group.id)
                .where(self.relationships_group.id == emp_group.ret_id())
            )
            basket_good_id = result.fetchall()
            brand = result.scalars().first()
            if brand:
                result = basket_good_id = session.execute(
                    insert(self.relationships_group).
                    values(**emp_group.dict()).
                    returning(self.relationships_group.id)
                )
                basket_good_id = result.fetchall()
            basket_good = session.execute(
                select(self.relationships_group)
                .where(self.relationships_group.id == basket_good_id[0][0])
            ).scalars().first()
            session.commit()
            return ResponseEmployeGroup(data=basket_good)

    def add_new_employee(self, new_emp: EmployeeCreateSchema, employe_group: List) -> str:
        res = "creatr"
        with self.get_db() as session:
            basket = self.base_model(**new_emp.dict(exclude={"group"}))
            session.add(basket)
            basket.group.extend(employe_group)
            session.commit()
            session.flush(basket)
            return basket
    


    def remove_employee(self, id: int) -> str:
        res = "remove"
        with self.get_db() as session:
            result = session.execute(
                select(self.base_model)
                .where(self.base_model.id == id)
            )
            client = result.scalars().first()
            # если есть объект то удаляем 
            if client:
                
                result = session.execute(
                    delete(self.test)
                    .where(self.test.c.emploeer_id == id)
                )
                result = session.execute(
                    delete(self.base_model)
                    .where(self.base_model.id == id)
                )

                res = "remove"
            else : 
                res = "id is not in table"
            session.commit()
        return res
    


    # def update_employee(self, client_data: EmployeeCreateSchema):
    #     res = "update"
    #     with self.get_db() as session:
    #         dict = client_data
    #         result = session.execute(
    #             select(self.base_model)
    #             .where(self.base_model.id == client_data.id)
    #         )
    #         print("date = ",client_data.dict())
    #         client = result.scalars().first()

    #         if client:
    #             result = session.execute(
    #                 update(self.base_model)
    #                 .where(self.base_model.id == client_data.id)
    #                 .values(client_data.dict(exclude={"group"})) # необходимо чтобы 
    #                 .returning(*self.base_model.__table__.c)
    #             )
                                  
    #             result = session.execute(
    #                 update(self.test)
    #                 .where(self.test.c.emploeer_id == client_data.id)
    #                 .values(client_data.dict({"id", "group.id"}))
    #             )
    #             res = "update"
    #         else : 
    #             res = "id is not in table"
    #         session.commit()
    #     return res

    def update_employee(self, client_data: EmployeeCreateSchema, employe_group: List):
        res = "update"
        with self.get_db() as session:
            basket = self.base_model(**client_data.dict(exclude={"group"}))
            result = session.execute(
                    update(self.base_model)
                    .where(self.base_model.id == client_data.id)
                    .values(client_data.dict(exclude={"group"})) # необходимо чтобы 
                    .returning(*self.base_model.__table__.c)
                )
            result = session.execute(
                    delete(self.test)
                    .where(self.test.c.emploeer_id == client_data.id)
                )
            for i in employe_group:
                result = session.execute(
                    insert(self.test)
                    .values(emploeer_id = client_data.id, id = i.id)
                    )
            basket.group.extend(employe_group)
            session.commit()
            session.flush(basket)
            return basket