import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from Telegram_API.handlers.command_handlers import command_router
from Telegram_API.handlers.mainDB_handlers import mainDB_router


async def startTelebot():

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(command_router, mainDB_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def message_sender(chat_id, message):
    try:
        await bot.send_message(chat_id, message)
        print("Сообщение отправлено успешно.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    asyncio.run(startTelebot())
