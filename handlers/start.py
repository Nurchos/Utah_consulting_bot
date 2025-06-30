from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from user_preferences import add_user, set_user_language  # импортируем обе функции

router = Router()

LANGS = {
    "ru": "🇷🇺 Русский",
    "ky": "🇰🇬 Кыргызча",
    "en": "🇬🇧 English",
    "es": "🇪🇸 Español",
}


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    add_user(message.from_user.id)

    keyboard = InlineKeyboardBuilder()
    for code, label in LANGS.items():
        keyboard.button(text=label, callback_data=f"lang:{code}")
    keyboard.adjust(2)

    await message.answer(
        "👋 Добро пожаловать! Выберите язык для уведомлений:",
        reply_markup=keyboard.as_markup()
    )


@router.callback_query(F.data.startswith("lang:"))
async def set_lang(callback: types.CallbackQuery):
    lang = callback.data.split(":")[1]
    set_user_language(callback.from_user.id, lang)

    response = {
        "ru": "✅ Язык установлен: Русский",
        "ky": "✅ Тил тандалды: Кыргызча",
        "en": "✅ Language set: English",
        "es": "✅ Idioma seleccionado: Español",
    }

    await callback.message.edit_text(response.get(lang, "✅ Язык установлен"))
