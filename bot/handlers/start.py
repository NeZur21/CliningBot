from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.main import main_reply_keyboard


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    name = message.from_user.first_name or "клиент"

    await message.answer(
        f"Здравствуйте, {name}! 👋\n\n"
        "Добро пожаловать в сервис клининга.\n\n"
        "Выберите нужную услугу:",
        reply_markup=main_reply_keyboard()
    )