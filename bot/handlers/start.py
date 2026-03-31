import asyncio

from aiogram import types, Router, F, Bot
from aiogram.filters import Command

import bot.keyboards.start_keyboards as kb

router = Router()


@router.message(Command("start"))
async def start_def(message: types.Message):
    await message.answer("""Привет. Выбери что-то""", reply_markup=kb.start_button)  # Когда будет много текста его надо будет вынести в отдельный файл и импортировать от туда