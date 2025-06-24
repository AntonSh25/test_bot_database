from environs import Env
from aiogram import Dispatcher, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from core import create_table, insert_users, insert_activities
import asyncio

import logging


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] #%(levelname)-8s %(filename)s:"
        "%(lineno)d - %(name)s - %(message)s",
    )

    logger = logging.getLogger(__name__)
    logger.info("Starting bot...")

    env = Env()

    dp = Dispatcher()
    bot = Bot(env.str("BOT_TOKEN"))

    @dp.message(CommandStart())
    async def cmd_start(message: Message):
        await insert_users(
            user_id=message.from_user.id,
            username=message.from_user.username,
        )
        par1 = message.from_user.id
        par2 = message.from_user.username
        await message.answer(
            text=f"Привет, тут будем тренироваться работать с БД PostgreSQL!\n"
            f"я записал твои данные в БД: \nuser_id={par1}, \nusername={par2}\n\n"
            f"Напиши мне еще, я все запишу..."
        )

    @dp.message()
    async def any_action(message: Message):
        await insert_activities(
            user_id=message.from_user.id,
            username=message.from_user.username,
            message_type=message.content_type,
            message_text=message.text,
        )
        await message.answer(
            text=f"так я реагирую на любое сообщение, кроме /start\n"
            f"Записал данные в БД, пиши еще!"
        )

    await create_table()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # dp.run_polling(bot)
    asyncio.run(main())
