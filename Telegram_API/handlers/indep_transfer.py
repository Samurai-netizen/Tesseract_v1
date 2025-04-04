from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from Telegram_API.chat_DB import devDBinit, firstInit, stateUpdate, stateFetch, newAmount, newArticle, fetchArgs, newSKUbond, newSKUaddChatdb

from Telegram_API.TBot_init import bot


async def message_sender(chat_id, message):
    try:
        await bot.send_message(chat_id, message)
        print("Сообщение отправлено успешно.")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")