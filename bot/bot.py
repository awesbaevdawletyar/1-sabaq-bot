"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def salem(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer("Assalawma a'leykum.Auesbaev Dawletyardin' botina xosh kelipsiz\n8a-oqiwshilarin salem")

@dp.message_handler(commands='help')
async def salem(message: types.Message):
    await message.answer("Sizge qanday jardem kerek?")
@dp.message_handler(commands='tel')
async def salem(message: types.Message):
    await message.answer("Bizge usi nomerler arqali qon'iraw etin'\n+9989138143743")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)