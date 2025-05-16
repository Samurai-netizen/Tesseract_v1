from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from Telegram_API.chat_DB import devDBinit, firstInit, stateUpdate, stateFetch, devDB_DROP

command_router = Router()


@command_router.message(Command("reload_chat_state_db"))
async def reload_chat_state_db_handler(msg: Message):
    try:
        devDBinit()
        await msg.answer("```Cоздана/обновлена БД для хранения состояний чатов```")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при создании/обновлении БД: {e}")


@command_router.message(Command("drop_chat_state_db"))
async def reload_chat_state_db_handler(msg: Message):
    try:
        devDB_DROP()
        await msg.answer("```Удалена БД для хранения состояний чатов```")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при создании/обновлении БД: {e}")


@command_router.message(Command("start"))
async def start_handler(msg: Message):
    try:
        firstInit(msg.from_user.id, msg.from_user.first_name, "start")
        await msg.answer("Привет! Меня зовут Тесса, я твой персональный ассистент. Я помогу тебе с автоматизацией бизнес-процессов.")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при инициализации: {e}")


@command_router.message(Command("testcom"))
async def testcom_handler(msg: Message):
    try:
        state = stateFetch(msg.from_user.id)
        if state is not None:
            await msg.answer(f"Твоё состояние чата со мной: {state}")
        else:
            await msg.answer("Состояние чата не найдено.")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при получении состояния: {e}")


@command_router.message(Command("state1"))
async def state1_handler(msg: Message):
    try:
        stateUpdate(msg.from_user.id, msg.from_user.first_name, "1")
        current_state = stateFetch(msg.from_user.id)
        await msg.answer(f"Текущее состояние чата: {current_state}")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при обновлении состояния: {e}")


@command_router.message(Command("state2"))
async def state2_handler(msg: Message):
    try:
        stateUpdate(msg.from_user.id, msg.from_user.first_name, "2")
        current_state = stateFetch(msg.from_user.id)
        await msg.answer(f"Текущее состояние чата: {current_state}")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при обновлении состояния: {e}")


@command_router.message(Command("check_stocks_fbs"))
async def check_stocks_fbs_handler(msg: Message):
    state = "check_stocks_fbs_1"
    stateUpdate(msg.from_user.id, msg.from_user.first_name, state)
    await msg.answer("Меню проверки остатков на складах Озон. Введите sku товара, который хотите проверить:")


@command_router.message(Command("add_new_item_pcs_to_db"))
async def add_new_item_pcs_to_db_handler(msg: Message):
    state = "add_new_item_pcs_to_db_1"
    stateUpdate(msg.from_user.id, msg.from_user.first_name, state)
    await msg.answer("Меню добавления закупленных товаров в БД склада. Введите артикул товара, который хотите добавить:")


@command_router.message(Command("declare_new_item_to_db"))
async def declare_new_item_to_db(msg: Message):
    state = "declare_new_item_to_db_1"
    stateUpdate(msg.from_user.id, msg.from_user.first_name, state)
    await msg.answer("Меню добавления новых товаров в БД склада. Введите артикул (название от продавца) товара, который хотите добавить:")