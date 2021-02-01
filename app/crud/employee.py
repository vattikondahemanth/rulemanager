from typing import List, Optional
from bson import ObjectId
from slugify import slugify
from datetime import datetime

from ..models.article import (
    ArticleFilterParams,
    ArticleInCreate,
    ArticleInDB,
    ArticleInUpdate,
)
from ..models.employee import (
    EmployeeInDB, ManyEmployeesInResponse, EmployeeInCreate
)
from ..models.pydanticmodels import PydanticObjectId
from ..models.helpers import create_employee_model
from ..db.mongodb import AsyncIOMotorClient
from ..core.config import database_name, favorites_collection_name, users_collection_name, article_collection_name, employee_collection_name
from .profile import get_profile_for_user
from .tag import (
    create_tags_that_not_exist,
    get_tags_for_article
)


async def get_employee_or_404(id: str, conn: AsyncIOMotorClient) -> EmployeeInDB:
    """
    Get Employee
    """
    employee = await conn[database_name][employee_collection_name].find_one({'_id': ObjectId(id)})
    if not employee:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Employee not found",
        )
    employee_model = create_employee_model(employee)
    return employee_model


async def get_employees(conn: AsyncIOMotorClient) -> ManyEmployeesInResponse:
    """
    Get Employees
    """
    employees = conn[database_name][employee_collection_name].find({}, limit=3, skip=1).sort("_id", 1)
    results = []
    async for employee in employees:
        results.append(create_employee_model(employee))
    return results

async def delete_employee(id: str, conn: AsyncIOMotorClient) -> dict:
    """
    Delete Employee
    """
    employee = await conn[database_name][employee_collection_name].find_one({"_id": ObjectId(id)})
    if not employee:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Employee not found",
        )
    
    await conn[database_name][employee_collection_name].delete_one({'_id': ObjectId(id)})
    return {"message": "Sucessfully Deleted"}

async def insert_employee(employee: dict, conn: AsyncIOMotorClient) -> dict:
    """
    Insert Employee
    """
    result = await conn[database_name][employee_collection_name].insert_one(employee)
    return {"message": "Sucessfully Created", "object_id": str(result.inserted_id)}


async def update_employee(employee: EmployeeInCreate, conn: AsyncIOMotorClient) -> dict:
    """
    Update Employee
    """
    employee = await conn[database_name][employee_collection_name].insert_one(employee)
    return {"message": "Sucessfully Created"}
