from fastapi import APIRouter, Body, Depends, Path
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from starlette.responses import JSONResponse

from ....core.jwt import get_current_user_authorizer
from ....core.utils import create_aliased_response
from ....crud.comment import create_comment, delete_comment, get_comments_for_article
from ....crud.shortcuts import get_article_or_404
from ....crud.employee import get_employee_or_404, get_employees, delete_employee, insert_employee
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....models.comment import (
    CommentInCreate,
    CommentInResponse,
    ManyCommentsInResponse,
)
from ....models.employee import (
    EmployeeInResponse, ManyEmployeesInResponse, EmployeeInCreate
)
from ....models.user import User

router = APIRouter()

"""
 Get Employee
"""
@router.get(
    "/employee/{id}",
    response_model=EmployeeInResponse,
    tags=["Employee"]
)
async def get_employee_api(
    id: str,
    db: AsyncIOMotorClient = Depends(get_database)
):
    employee = await get_employee_or_404(id, db)
    print(employee)
    return create_aliased_response(EmployeeInResponse(employee=employee))

"""
 Get Employees
"""
@router.get(
    "/employees",
    response_model=ManyEmployeesInResponse,
    tags=["Employee"]
)
async def get_employees_api(
    db: AsyncIOMotorClient = Depends(get_database),
):
    employees = await get_employees(db)
    print(employees)
    return create_aliased_response(ManyEmployeesInResponse(employees=employees))

"""
 Delete an Employee
"""
@router.delete(
    "/employee/delete/{id}",
    response_model=dict,
    tags=["Employee"]
)
async def delete_employee_api(
    id: str,
    db: AsyncIOMotorClient = Depends(get_database)
):
    result = await delete_employee(id, db)
    return JSONResponse(content=result)

"""
 Insert an Employee
""" 
@router.post(
    "/employee/insert",
    response_model=dict,
    status_code=HTTP_201_CREATED,
    tags=["Employee"]
)
async def insert_employee_api(
    employee: EmployeeInCreate = Body(..., embed=True),
    db: AsyncIOMotorClient = Depends(get_database)
):
    result = await insert_employee(employee.dict(), db)
    return JSONResponse(content=result)
