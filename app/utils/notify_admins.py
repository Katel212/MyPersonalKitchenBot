from typing import List
from app.utils import Broadcast
from loguru import logger


async def notify_admins(admins: List[int]):
    count = await (Broadcast(admins, 'The bot is running!')).start()
    logger.info(f"{count} admins received messages")
