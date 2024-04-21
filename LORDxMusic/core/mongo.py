from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER("مـيـوزك لـورد").info("جـارِ الاتصـال بقاعـدة البيانـات . . .⁦♡")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER("مـيـوزك لـورد").info("تم الاتصـال بقاعـدة البيانـات ...⁦♡")
except:
    LOGGER("مـيـوزك لـورد").error("حدث خطأ اثناء الاتصال بقاعدة البيانات.")
    exit()
