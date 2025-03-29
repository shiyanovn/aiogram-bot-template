import json
from typing import Optional, get_args
from uuid import UUID

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo
from pydantic import BaseModel


async def start(msg: Message,):
    print(1)