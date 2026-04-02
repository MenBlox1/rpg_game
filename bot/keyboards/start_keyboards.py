from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

start_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вперёд!', callback_data="go_button")]
])

sex_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Посудомойка", callback_data="sex_woman"),
        InlineKeyboardButton(text="Насильник", callback_data="sex_man")
    ]
])

class_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Воин", callback_data="class_voin"),
        InlineKeyboardButton(text="Маг", callback_data="class_mag")
    ],

    [
        InlineKeyboardButton(text="Лучник", callback_data="class_archer"),
        InlineKeyboardButton(text="Бомжиха", callback_data="class_bomjixa")
    ]
])

start_game_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='К приключениям!', callback_data="game_button")]
])

game_map_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data="map_button")]
])