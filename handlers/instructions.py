from aiogram import Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
from user_preferences import get_user_language

router = Router()

# Локализованные инструкции
PROBLEM_INSTRUCTIONS = {
    "no_sound": {
        "ru": "🔇 Если нет звука:\n1. Проверьте громкость.\n2. Перезагрузите устройство.\n3. Проверьте наушники.",
        "en": "🔇 No sound:\n1. Check the volume.\n2. Restart the device.\n3. Check your headphones.",
        "ky": "🔇 Үн жок болсо:\n1. Үн деңгээлин текшериңиз.\n2. Аппаратыңызды өчүрүп күйгүзүңүз.\n3. Наушнигиңизди текшериңиз.",
        "es": "🔇 Sin sonido:\n1. Verifica el volumen.\n2. Reinicia el dispositivo.\n3. Revisa tus auriculares.",
    },
    "no_connection": {
        "ru": "📶 Если нет соединения:\n1. Включите Wi-Fi или мобильный интернет.\n2. Перезапустите роутер.",
        "en": "📶 No connection:\n1. Turn on Wi-Fi or mobile data.\n2. Restart your router.",
        "ky": "📶 Байланыш жок болсо:\n1. Wi-Fi же мобилдик интернетти күйгүзүңүз.\n2. Роутерди өчүрүп күйгүзүңүз.",
        "es": "📶 Sin conexión:\n1. Activa Wi-Fi o datos móviles.\n2. Reinicia el router.",
    },
    "app_crash": {
        "ru": "💥 Если приложение вылетает:\n1. Обновите приложение.\n2. Очистите кеш.\n3. Переустановите приложение.",
        "en": "💥 App crashes:\n1. Update the app.\n2. Clear the cache.\n3. Reinstall the app.",
        "ky": "💥 Эгер тиркеме жабылып калса:\n1. Тиркемени жаңыртыңыз.\n2. Кэшти тазалаңыз.\n3. Тиркемени кайра орнотуңуз.",
        "es": "💥 La app falla:\n1. Actualiza la app.\n2. Limpia la caché.\n3. Reinstala la app.",
    }
}

# Переводы текста кнопок
PROBLEM_BUTTONS = {
    "no_sound": {
        "ru": "🔇 Нет звука",
        "en": "🔇 No Sound",
        "ky": "🔇 Үн жок",
        "es": "🔇 Sin sonido",
    },
    "no_connection": {
        "ru": "📶 Нет соединения",
        "en": "📶 No Connection",
        "ky": "📶 Байланыш жок",
        "es": "📶 Sin conexión",
    },
    "app_crash": {
        "ru": "💥 Приложение вылетает",
        "en": "💥 App Crashes",
        "ky": "💥 Тиркеме жабылууда",
        "es": "💥 Falla la app",
    }
}

# Переводы заголовка
INSTRUCTION_TITLES = {
    "ru": "Выберите проблему, с которой вы столкнулись:",
    "en": "Choose the problem you are facing:",
    "ky": "Сизди кызыктырган маселени тандаңыз:",
    "es": "Selecciona el problema que tienes:",
}


@router.message(Command("instructions"))
async def show_problem_buttons(message: types.Message):
    lang = get_user_language(message.from_user.id)
    lang = lang if lang in ["ru", "en", "ky", "es"] else "ru"  # fallback

    # Строим локализованные кнопки
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=PROBLEM_BUTTONS["no_sound"][lang], callback_data="no_sound")],
            [InlineKeyboardButton(text=PROBLEM_BUTTONS["no_connection"][lang], callback_data="no_connection")],
            [InlineKeyboardButton(text=PROBLEM_BUTTONS["app_crash"][lang], callback_data="app_crash")],
        ]
    )

    await message.answer(INSTRUCTION_TITLES[lang], reply_markup=keyboard)


@router.callback_query()
async def handle_problem_selection(callback: CallbackQuery):
    lang = get_user_language(callback.from_user.id)
    lang = lang if lang in ["ru", "en", "ky", "es"] else "ru"  # fallback

    instruction = PROBLEM_INSTRUCTIONS.get(callback.data, {}).get(lang)
    if instruction:
        await callback.message.edit_text(instruction)
    else:
        await callback.answer("Неизвестная команда.")
