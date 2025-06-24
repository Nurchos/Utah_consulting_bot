from aiogram import Router, types
from aiogram.filters import Command
from user_storage import get_all_users

router = Router()


@router.message(Command("notify_all"))
async def notify_all_users(message: types.Message):
    if message.from_user.id != 1971434104:
        await message.answer("❌ У вас нет прав на отправку рассылки.")
        return

    users = get_all_users()
    for user_id in users:
        try:
            await message.bot.send_message(
                chat_id=user_id,
                text="🚨 Не забудьте расписаться в приложении, чтобы избежать нарушений!"
            )
        except Exception as e:
            print(f"❗ Не удалось отправить пользователю {user_id}: {e}")

    await message.answer("✅ Напоминание отправлено всем зарегистрированным водителям.")
