from typing import List
from .pydanticmodels import PydanticObjectId

from .dbmodel import DBModelMixin, DateTimeModelMixin
from .profile import Profile
from .rwmodel import RWModel


class EmployeeInDB(DateTimeModelMixin):
	object_id: PydanticObjectId = None
	id: int = None
	name: str = None
	department: str = None


class Employee(DateTimeModelMixin):
	id: int = None
	name: str = None
	department: str = None
    

class EmployeeInCreate(Employee):
    pass


class EmployeeInResponse(RWModel):
    employee: EmployeeInDB


class ManyEmployeesInResponse(RWModel):
    employees: List[EmployeeInDB]
