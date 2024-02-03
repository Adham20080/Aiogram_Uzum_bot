import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from config import Token
from aiogram.types import Message
from button import button
from button import btn1

bot = Bot(token=Token)

dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer_photo(photo="https://images.app.goo.gl/BzpMtZdoGCiPusTT6",
                               caption=f"Assalomu alaykum {message.from_user.full_name} Bizning 🏪 Uzum Market botimizga xush kelibsiz 👋",
                               reply_markup=button)


@dp.message(F.text == "Telefonlar")
async def phones(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/clmsv4nn7c6gg9idnb40/original.jpg",
                               caption="Smartfon vivo Y27s 8/128GB, 90Hz display",
                               reply_markup=btn1)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
