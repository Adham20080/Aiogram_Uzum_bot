from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Smartfon vivo Y27s 8/128GB, 90Hz display',
                          url="https://images.uzum.uz/cli250t6sfhvbd1j62jg/original.jpg")],
])

btn = [
    [types.KeyboardButton(text="Telefonlar"), types.KeyboardButton(text="Aksusuarlar")],

]
button = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)

btn1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Smartfon vivo Y27s",
                          url="https://uzum.uz/uz/product/smartfon-vivo-y27s-8128gb-90hz-display-832698?skuid=2093119")]

])
