from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums.content_type import ContentType
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode

import json

webapp = Router()


@webapp.message(Command("webapp"))
async def start(msg: Message):
    webAppInfo = types.WebAppInfo(url="https://ec3d-45-14-71-11.ngrok-free.app")
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Отправить данные', web_app=webAppInfo))
    print("gocha!")

    await msg.answer(text='Привет!', reply_markup=builder.as_markup())


@webapp.message(F.content_type == ContentType.WEB_APP_DATA)
async def parse_data(msg: Message):
    data = json.loads(msg.web_app_data.data)
    print("gocha!!!")
    print(data["name"], type(data["name"]))
    print(data["amount"], type(data["amount"]))
    print(data["price_rmb_1pcs"], type(data["price_rmb_1pcs"]))
    print(data["price_rmb_total"], type(data["price_rmb_total"]))
    print(data["if_paid"], type(data["if_paid"]))
    print(data["shipment_id"], type(data["shipment_id"]))
    print(data["total_mass_kg"], type(data["total_mass_kg"]))
    print(data["if_picked_up"], type(data["if_picked_up"]))
    print(data["if_problems"], type(data["if_problems"]))

    await msg.answer(f'<b>{data["name"]}</b>\n\n<code>{data["amount"]}</code>\n\n{data["if_problems"]}', parse_mode=ParseMode.HTML)
