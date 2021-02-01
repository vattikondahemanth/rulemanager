import logging

from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db


async def connect_to_mongo():
	print("Trying to connect to Mongo...")
	logging.info("Trying to connect to Mongo...")
	db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
	logging.info("Connected Successfully...")
	print("Connected Successfully...")


async def close_mongo_connection():
    logging.info("Trying to close Mongo...")
    db.client.close()
    logging.info("Successfully closed！")
