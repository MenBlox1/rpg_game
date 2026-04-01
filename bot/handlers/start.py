import asyncio

from aiogram import types, Router, F, Bot
from aiogram.filters import Command

import bot.keyboards.start_keyboards as kb
import bot.handlers.texts

router = Router()


@router.message(Command("start"))
async def start_def(message: types.Message):
    await message.answer(text=texts.text_1, reply_markup=kb.start_button)  # Когда будет много текста его надо будет вынести в отдельный файл и импортировать от туда