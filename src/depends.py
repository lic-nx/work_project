from services.employee import EmployeeService
from services.group import GroupService
from services.carts import CartsService
from database.db import get_db
from repository.employee import EmployeeRepositoriy
from repository.carts import CartsRepositoriy
from repository.group import GroupRepositoriy
employee_repository = EmployeeRepositoriy(get_db)
carts_repository = CartsRepositoriy(get_db)
group_repository= GroupRepositoriy(get_db)

employee_service = EmployeeService(
    employee_repository
)

group_service = GroupService(
    group_repository
)

carts_service = CartsService(
    carts_repository
)

def get_group_service() -> GroupService:
    return group_service 


def get_employee_service() -> EmployeeService:
    return employee_service


def get_carts_service() -> CartsService:
    return carts_service