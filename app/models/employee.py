from typing import List

from .dbmodel import DBModelMixin
from .profile import Profile
from .rwmodel import RWModel


class EmployeeInDB(RWModel):
	_id: str
	name: str
	department: str


class Employee(EmployeeInDB):
    pass


class EmployeeInCreate(RWModel):
    body: str


class EmployeeInResponse(RWModel):
    employee: Employee


class ManyEmployeesInResponse(RWModel):
    employees: List[Employee]
