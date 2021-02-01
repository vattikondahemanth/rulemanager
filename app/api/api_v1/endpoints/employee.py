from fastapi import APIRouter, Body, Depends, Path
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from ....core.jwt import get_current_user_authorizer
from ....core.utils import create_aliased_response
from ....crud.comment import create_comment, delete_comment, get_comments_for_article
from ....crud.shortcuts import get_article_or_404, get_employee_or_404
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....models.comment import (
    CommentInCreate,
    CommentInResponse,
    ManyCommentsInResponse,
)
from ....models.employee import (
    EmployeeInResponse
)
from ....models.user import User

router = APIRouter()

@router.get(
    "/test/employee",
    response_model=EmployeeInResponse,
    tags=["comments"],
)
async def get_empoyee(
    db: AsyncIOMotorClient = Depends(get_database),
):
    employee = await get_employee_or_404(db)
    return create_aliased_response(EmployeeInResponse(employee=employee))
