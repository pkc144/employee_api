from fastapi import APIRouter, Query
from .models import Employee, UpdateEmployee
from . import services

router = APIRouter()

#post request
@router.post("/employees")
def create_employee(emp: Employee):
    return services.create_employee(emp)

# get requests
@router.get("/employees/avg-salary")
def avg_salary_by_department():
    return services.avg_salary_by_department()

@router.get("/employees/search")
def search_by_skill(skill: str):
    return services.search_by_skill(skill)

@router.get("/employees")
def list_employees(
    department: str = Query(None),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max records to return"),
):
    return services.list_employees(department, skip, limit)


@router.get("/employees/{employee_id}")
def get_employee(employee_id: str):
    return services.get_employee(employee_id)

#update  employee route
@router.put("/employees/{employee_id}")
def update_employee(employee_id: str, updates: UpdateEmployee):
    return services.update_employee(employee_id, updates)

#delete employee route
@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: str):
    return services.delete_employee(employee_id)

