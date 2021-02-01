from .employee import EmployeeInDB
from .pydanticmodels import PydanticObjectId

def create_employee_model(employee):
	return EmployeeInDB(
            object_id = PydanticObjectId(employee["_id"]),
            id = employee.get("id", None),
            name = employee.get("name", None),
            department = employee.get("department", None),
            created_at = employee.get("created_at", None),
            updated_at = employee.get("updated_at", None)
        )
