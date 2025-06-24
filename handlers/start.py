from aiogram import Router, types
from aiogram.filters import Command
from user_storage import add_user

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    add_user(message.from_user.id)
    await message.answer("👋 Добро пожаловать! Вы зарегистрированы для уведомлений.")
