from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.data.db.connection.session import get_session
from app.data.db.models.user import User
from app.loader import dp

router = Router()

@dp.message(Command("adduser"))
async def add_user(message: Message):
    args = message.text.split()
    if len(args) < 3:
        await message.answer("Используйте: /adduser <username> <first_name> [last_name]")
        return

    username = args[1]
    first_name = args[2]
    last_name = args[3] if len(args) > 3 else None

    # Получаем сессию с помощью get_session
    async with get_session() as session:
        # Проверяем, есть ли уже такой пользователь
        result = await session.execute(select(User).where(User.username == username))
        existing_user = result.scalars().first()

        if existing_user:
            await message.answer(f"❌ Пользователь {username} уже существует!")
            return

        # Создаём нового пользователя
        new_user = User(
            id=message.from_user.id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        session.add(new_user)
        await session.commit()

        await message.answer(f"✅ Пользователь {username} добавлен!")

