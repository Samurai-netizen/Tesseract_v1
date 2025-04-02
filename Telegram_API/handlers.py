from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from chat_DB import devDBinit, firstInit, stateUpdate, stateFetch

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    firstInit(msg.from_user.id, msg.from_user.first_name, "start")
    await msg.answer("Привет! Меня зовут Тесса, я твой персональный ассистент. Я помогу тебе с автоматизацией бизнес-процессов.")


@router.message(Command("testcom"))
async def start_handler(msg: Message):
    await msg.answer(f"Твоё состояние чата со мной: {stateFetch(msg.from_user.id)}")


@router.message(Command("state1"))
async def start_handler(msg: Message):
    state = "1"
    stateUpdate(msg.from_user.id, msg.from_user.first_name, state)
    await msg.answer(f"Текущее состояние чата: {stateFetch(msg.from_user.id)}")


@router.message(Command("state2"))
async def start_handler(msg: Message):
    state = "2"
    stateUpdate(msg.from_user.id, msg.from_user.first_name, state)
    await msg.answer(f"Текущее состояние чата: {stateFetch(msg.from_user.id)}")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")