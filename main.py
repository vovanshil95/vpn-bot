import logging
import asyncio
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import API_TOKEN, SERVICE_HOST

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    download_button = InlineKeyboardButton(text="Скачать приложение",
                                           url=f'https://{SERVICE_HOST}/app')
    connect_button = InlineKeyboardButton(text="Подключить vpn",
                                          url=f'https://{SERVICE_HOST}/config/{message.chat.id}')
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[[download_button],[connect_button]])
    await message.answer("Привет! Для начала работы с нашим VPN, пожалуйста, выполните следующие шаги:\n\n1. Нажмите на верхнюю кнопку, чтобы скачать приложение.\n2. После установки приложения, нажмите на вторую кнопку, чтобы подключиться", reply_markup=inline_kb)

async def main() -> None:
    bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
