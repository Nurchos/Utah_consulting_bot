from aiogram import Router, types
from aiogram.filters import Command
from user_preferences import get_all_users, get_user_language  # импортируем нужные функции

router = Router()

ADMIN_ID = 1971434104  # замени на свой ID при необходимости

# Сообщения на разных языках
MESSAGES = {
    "ru": "🚨 Не забудьте расписаться в приложении, чтобы избежать нарушений!",
    "ky": "🚨 Тиркемеге кол коюуну унутпаңыз, эреже бузбоо үчүн!",
    "en": "🚨 Don’t forget to check in the app to avoid violations!",
    "es": "🚨 ¡No olvides firmar en la app para evitar infracciones!\n\n🚨 Не забудьте расписаться в приложении!\n🚨 Don’t forget to sign in the app!",
    "tr": "🚨 İhlallerden kaçınmak için uygulamaya giriş yapmayı unutmayın!"
}


@router.message(Command("notify_all"))
async def notify_all_users(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ У вас нет прав на отправку рассылки.")
        return

    users = get_all_users()
    count = 0
    for user_id in users:
        lang = get_user_language(user_id)
        text = MESSAGES.get(lang, MESSAGES["ru"])  # по умолчанию русский
        try:
            await message.bot.send_message(chat_id=user_id, text=text)
            count += 1
        except Exception as e:
            print(f"❗ Не удалось отправить пользователю {user_id}: {e}")

    await message.answer(f"✅ Напоминание отправлено {count} водителям.")
