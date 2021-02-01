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
    EmployeeInDB,
)

from ..db.mongodb import AsyncIOMotorClient
from ..core.config import database_name, favorites_collection_name, users_collection_name, article_collection_name, employee_collection_name
from .profile import get_profile_for_user
from .tag import (
    create_tags_that_not_exist,
    get_tags_for_article
)


async def get_employee_by_slug(conn: AsyncIOMotorClient) -> EmployeeInDB:
    employee = await conn[database_name][employee_collection_name].find_one({})
    return EmployeeInDB(
            **employee,
            created_at=ObjectId(employee["_id"]).generation_time
        )