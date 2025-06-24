from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command

router = Router()

# Проблемы и инструкции
PROBLEM_INSTRUCTIONS = {
    "no_sound": "🔇 Если нет звука:\n1. Проверьте громкость.\n2. Перезагрузите устройство.\n3. Проверьте наушники.",
    "no_connection": "📶 Если нет соединения:\n1. Включите Wi-Fi или мобильный интернет.\n2. Перезапустите роутер.",
    "app_crash": "💥 Если приложение вылетает:\n1. Обновите приложение.\n2. Очистите кеш.\n3. Переустановите приложение.",
}


# Команда /instructions показывает кнопки с проблемами
@router.message(Command("instructions"))
async def show_problem_buttons(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔇 Нет звука", callback_data="no_sound")],
            [InlineKeyboardButton(text="📶 Нет соединения", callback_data="no_connection")],
            [InlineKeyboardButton(text="💥 Приложение вылетает", callback_data="app_crash")],
        ]
    )
    await message.answer("Выберите проблему, с которой вы столкнулись:", reply_markup=keyboard)


# Обработка нажатий на кнопки
@router.callback_query()
async def handle_problem_selection(callback: CallbackQuery):
    instruction = PROBLEM_INSTRUCTIONS.get(callback.data)
    if instruction:
        await callback.message.edit_text(instruction)
    else:
        await callback.answer("Неизвестная команда.")
