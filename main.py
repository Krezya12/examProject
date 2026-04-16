import asyncio
import logging
import sys
from os import getenv

from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext as _, I18n, lazy_gettext as __

from keyboards import *
from classes import States

load_dotenv()

i18n = I18n(path="locales", default_locale="ru", domain="locales")
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


# @dp.message(CommandStart())
# async def start(message: Message) -> None:
#     await message.answer("Выберите язык:", markup=lang())

@dp.message(CommandStart())
async def main(message: Message, state: FSMContext):
    await message.answer("Главное меню", reply_markup=mainm())


@dp.callback_query(F.data == "btmm")
async def main(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text("Главное меню", reply_markup=mainm())


@dp.callback_query((F.data == "rm") | (F.data == "btrm"))
async def main(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text("Меню ресторана:", reply_markup=catalogs())

@dp.callback_query((F.data == "salat"))
async def main(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text("Салаты", reply_markup=salats())


@dp.callback_query((F.data == "ff"))
async def main(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text("Еда быстрого приготовления", reply_markup=fast_food())


@dp.callback_query((F.data == "he"))
async def main(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text("Горячие блюда", reply_markup=hotd())

@dp.callback_query((F.data == "cs"))
async def main(message: Message, state: FSMContext):
    await message.answer("Отправьте сообщение, мы обязательно прочитаем")
    await state.set_state(States.text)


@dp.message(States.text)
async def feedback_received(message: Message, state: FSMContext, bot: Bot):

    await bot.send_message(
        chat_id=getenv("ADMIN_ID"),
        text=f"Новый отзыв от @{message.from_user.username}:\n\n{message.text}"
    )

    await message.answer("Ваше сообщение отправлено!")
    await state.clear()





async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())