from pydantic import BaseModel
from bson.objectid import ObjectId

class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required but received {}'.format(str(type(v))))
        return v