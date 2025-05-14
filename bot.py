import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = "7964458353:AAH6erJIKPJbZREyXvIASCc4Y-vpn1FRA0o"

CHANNEL_ID = -1002628842649

from aiogram.client.default import DefaultBotProperties
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message()
async def handle_message(message: Message):
    text = f"<b>Анонимное сообщение:</b>\n{message.text}"
    await bot.send_message(CHANNEL_ID, text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
