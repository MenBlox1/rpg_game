import asyncio
from pathlib import Path
from aiogram import types, Router, F, Bot
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import bot.keyboards.start_keyboards as kb
import bot.handlers.texts as texts

router = Router()

class Reg(StatesGroup):
    name = State()


@router.message(Command("start"))
async def start_def(message: types.Message):
    photo = FSInputFile("bot/images/1 Заставка.png")
    await message.answer_photo(
        photo=photo,
        caption=texts.вступительный_текст,
        reply_markup=kb.start_button
    )


@router.callback_query(F.data == "go_button")
async def go_button(callback: types.CallbackQuery):
    photo = FSInputFile("bot/images/2 Пол.jpg")
    await callback.answer()
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo,
            caption=texts.выбор_пола
        ),
        reply_markup=kb.sex_button
    )



@router.callback_query(F.data.startswith("sex_"))
async def choose_sex(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    sex_choice = callback.data.replace("sex_", "")
    
    await state.update_data(sex=sex_choice, reg_message_id=callback.message.message_id)

    photo = FSInputFile("bot/images/3 Имя.jpg")
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo,
            caption=texts.ввод_имени
        ),
        reply_markup=None
    )

    await state.set_state(Reg.name)



@router.message(Reg.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    data = await state.get_data()
    sex = data.get("sex")
    name = data.get("name")
    reg_message_id = data.get("reg_message_id")

    photo = FSInputFile("bot/images/4 Классы.jpg")

    await message.bot.edit_message_media(
        chat_id=message.chat.id,
        message_id=reg_message_id,
        media=types.InputMediaPhoto(
            media=photo,
            caption=texts.выбор_класса
        ),
        reply_markup=kb.class_button
    )

    
    await message.delete()



@router.callback_query(F.data.startswith("class_"))
async def choose_class(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    class_choice = callback.data.replace("class_", "")
    await state.update_data(class_=class_choice)

    data = await state.get_data()
    sex = data.get("sex")
    name = data.get("name")

    photo = FSInputFile("bot/images/5 Персонаж.jpg")
    text = (
        "✅ Персонаж создан!\n\n"
        f"👤 Имя: {name}\n"
        f"⚥ Пол: {sex}\n"
        f"🛡 Класс: {class_choice}"
    )

    reg_message_id = data.get("reg_message_id")
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo,
            caption=text
        ),
        reply_markup=kb.start_game_button
    )

    
    await state.clear()


@router.callback_query(F.data == "game_button")
async def go_button(callback: types.CallbackQuery):
    photo = FSInputFile("bot/images/6 Начало.jpeg")
    await callback.answer()
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=photo,
            caption=texts.история_игры
        ),
        reply_markup=kb.game_map_button
    )