from services.employee import EmployeeService
from database.db import get_db
from repository.employee import EmployeeRepositoriy

employee_repository = EmployeeRepositoriy(get_db)

employee_service = EmployeeService(
    employee_repository
)

def get_employee_service() -> EmployeeService:
    return employee_service