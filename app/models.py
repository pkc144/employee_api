from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Employee(BaseModel):
    employee_id: str = Field(..., description="Unique Employee ID")
    name: str
    department: str
    salary: float
    joining_date: datetime
    skills: List[str]

class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    joining_date: Optional[datetime] = None
    skills: Optional[List[str]] = None
