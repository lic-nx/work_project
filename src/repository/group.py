from typing import List
from database.models.employee import *
from schemas.employee import GroupCreateSchema
from sqlalchemy.future import select
from sqlalchemy import and_, func, insert, update, join, delete
from sqlalchemy.orm import joinedload

from typing import NamedTuple, Union, List, Dict


class GroupRepositoriy:
    base_model = Group

    def __init__(self, get_db):
        self.get_db = get_db

        
    def add_new_group(self, emp_group: GroupCreateSchema)->str:
        with self.get_db() as session:
            session.execute(
                insert(self.base_model).
                values(**emp_group.dict())
            )
            session.commit()
        return "done"