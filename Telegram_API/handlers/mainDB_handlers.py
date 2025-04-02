from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from Telegram_API.chat_DB import devDBinit, firstInit, stateUpdate, stateFetch

from Ozon_API.API_requests_list import v1_product_info_stocks_by_warehouse_fbs

mainDB_router = Router()

@mainDB_router.message(Command("state2"))
async def state2_handler(msg: Message):
    try:
        state = "2"
        stateUpdate(msg.from_user.id, msg.from_user.first_name, state)
        current_state = stateFetch(msg.from_user.id)
        await msg.answer(f"Текущее состояние чата: {current_state}")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при обновлении состояния: {e}")


@mainDB_router.message()
async def message_handler(msg: Message):
    try:
        current_state = stateFetch(msg.from_user.id)
        match current_state:

            case "start":
                pass

            case "check_stocks_1":
                output = await v1_product_info_stocks_by_warehouse_fbs(msg.text)
                await msg.answer(f"{output}")


        await msg.answer(f"Твой ID: {msg.from_user.id}")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при обработке сообщения: {e}")
