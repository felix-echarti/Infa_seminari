from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_welcome(message: types.Message):
    await message.reply("Tell me something!")
