from repository.employee import EmployeeRepositoriy
from schemas.employee import EmployeeCreateSchema

from typing import List


class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepositoriy,) -> None:
        self.employee_repository = employee_repository

    def get_all_employee(self) -> List[EmployeeCreateSchema]:
        employee = self.employee_repository.get_all_employee()
        return employee
    
    def add_new_employee(self, client_data: EmployeeCreateSchema)->str:
        try:
            employee = self.employee_repository.add_new_employee(client_data)
        except:
            return "err to add"
        return employee


    def remove_employee(self, id: int)->str:
        try:
            employee = self.employee_repository.remove_employee(id)
        except:
            return "err to remove"
        return employee
