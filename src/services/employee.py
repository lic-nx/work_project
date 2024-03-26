from repository.employee import EmployeeRepositoriy
from schemas.employee import *

from typing import List


class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepositoriy,) -> None:
        self.employee_repository = employee_repository

    def get_all_employee(self) -> List[EmployeeCreateSchema]:
        employee = self.employee_repository.get_all_employee()
        employee = [EmployeeCreateSchema.from_orm(employee) for employee in employee]
        return employee
    
    def add_new_employee(self, client_data: EmployeeCreateSchema):
        # try:
        # group = [GroupResponseSchema.from_orm(brand) for brand in client_data.group]
        emplouer_group = client_data.group
        employer_group_list: List = [self.employee_repository.create_emplouer_group(emplouer_grouup).data 
                                     for emplouer_grouup in emplouer_group ]
        employee = self.employee_repository.add_new_employee(client_data, employer_group_list)

        return "done"


    def remove_employee(self, id: int)->str:
        employee = self.employee_repository.remove_employee(id)
        
        return employee

    def update_employee(self, client_data: EmployeeCreateSchema)->str:
        emplouer_group = client_data.group
        employer_group_list: List = [self.employee_repository.create_emplouer_group(emplouer_grouup).data 
                                     for emplouer_grouup in emplouer_group ]
        employee = self.employee_repository.update_employee(client_data, employer_group_list)
        
        return employee
    

