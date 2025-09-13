from fastapi import HTTPException
from .db import collection
from .models import Employee, UpdateEmployee

# Create Employee
def create_employee(emp: Employee):
    if collection.find_one({"employee_id": emp.employee_id}):
        raise HTTPException(status_code=400, detail="Employee ID already exists")
    collection.insert_one(emp.dict())
    return {"message": "Employee created successfully"}

# Get Employee by ID
def get_employee(employee_id: str):
    employee = collection.find_one({"employee_id": employee_id}, {"_id": 0})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Update Employee
def update_employee(employee_id: str, updates: UpdateEmployee):
    update_data = {k: v for k, v in updates.dict().items() if v is not None}
    result = collection.update_one({"employee_id": employee_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee updated successfully"}

# Delete Employee
def delete_employee(employee_id: str):
    result = collection.delete_one({"employee_id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}

# List Employees by Department
def list_employees(department: str = None, skip: int = 0, limit: int = 10):
    query = {}
    if department:
        query["department"] = department
    employees = list(
        collection.find(query, {"_id": 0})
        .sort("joining_date", -1)
        .skip(skip)
        .limit(limit)
    )
    return employees

# Average Salary by Department
def avg_salary_by_department():
    pipeline = [
        {"$group": {"_id": "$department", "avg_salary": {"$avg": "$salary"}}},
        {"$project": {"_id": 0, "department": "$_id", "avg_salary": 1}}
    ]
    return list(collection.aggregate(pipeline))

# Search Employees by Skill
def search_by_skill(skill: str):
    employees = list(collection.find(
        {"skills": {"$regex": f"^{skill}$", "$options": "i"}},  # match regardless of case
        {"_id": 0}
    ))
    return employees
