from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from Telegram_API.chat_DB import devDBinit, firstInit, stateUpdate, stateFetch, newAmount, newArticle, fetchArgs, newSKUbond, newSKUaddChatdb, fetchArticle, fetchSku

from Database.DB_Conn import db_insert

from Ozon_API.API_requests_list import v1_product_info_stocks_by_warehouse_fbs

mainDB_router = Router()

''''@mainDB_router.message(Command("state2"))
async def state2_handler(msg: Message):
    try:
        stateUpdate(msg.from_user.id, msg.from_user.first_name, "2")
        current_state = stateFetch(msg.from_user.id)
        await msg.answer(f"Текущее состояние чата: {current_state}")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при обновлении состояния: {e}")'''


@mainDB_router.message()
async def message_handler(msg: Message):
    current_state = stateFetch(msg.from_user.id)
    match current_state:

        case "start":
            print("---Start case detected (placeholder idk)")

        case "check_stocks_fbs_1":
            if msg.text != "Назад":
                sku = fetchSku(msg.from_user.id, msg.text)
                output = await v1_product_info_stocks_by_warehouse_fbs(sku)
                print(output)
                await msg.answer(f"{output}")
            else:
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "homescreen")

        case "add_new_item_pcs_to_db_1":
            if msg.text != "Назад":
                newArticle(msg.from_user.id, msg.text)
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "add_new_item_pcs_to_db_2")
                await msg.answer(f'Введите количество товара:')

            else:
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "homescreen")

        case "add_new_item_pcs_to_db_2":
            if msg.text != "Назад":
                newAmount(msg.from_user.id, msg.text)
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "add_new_item_pcs_to_db_3")
                temp = fetchArgs(msg.from_user.id)
                await db_insert(temp[0], temp[1], temp[2])
                await msg.answer(f'Данные будут введены в систему учёта склада')
            else:
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "homescreen")

        case "declare_new_item_to_db_1":
            if msg.text != "Назад":
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "declare_new_item_to_db_2")
                await msg.answer(f'Введите SKU товара, который хотите добавить:')
                newSKUaddChatdb(msg.from_user.id, msg.text)
            else:
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "homescreen")

        case "declare_new_item_to_db_2":
            if msg.text != "Назад":
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "add_new_item_pcs_to_db_3")
                await msg.answer(f'Новая пара SKU-артикул добавлена. Теперь вы можете добавить остатки товара')
                newSKUbond(msg.from_user.id, msg.text)
            else:
                stateUpdate(msg.from_user.id, msg.from_user.first_name, "homescreen")

    try:
        state = stateFetch(msg.from_user.id)
        if state is not None:
            await msg.answer(f"Твоё состояние чата со мной: {state}")
        else:
            await msg.answer("Состояние чата не найдено.")
    except Exception as e:
        await msg.answer(f"Произошла ошибка при получении состояния: {e}")

