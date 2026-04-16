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
from aiogram.utils.i18n import gettext as _, I18n, lazy_gettext as __, FSMI18nMiddleware

from keyboards import *
from classes import States

load_dotenv()

i18n = I18n(path="locales", default_locale="ru", domain="messages")
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


@dp.callback_query(F.data == "uz")
async def set_lang(call: CallbackQuery, state: FSMContext, i18n: I18n):
    lang_code = "uz"
    await state.update_data(locale=lang_code)
    await call.answer(_("Til o'zgartirildi", locale=lang_code))
    await call.message.edit_text(_("Asosiy menyu", locale=lang_code), reply_markup=mainm())


@dp.callback_query(F.data == "en")
async def set_lang(call: CallbackQuery, state: FSMContext, i18n: I18n):
    lang_code = "en"
    await state.update_data(locale=lang_code)
    await call.answer(_("Language changed", locale=lang_code))
    await call.message.edit_text(_("Main menu", locale=lang_code), reply_markup=mainm())


@dp.callback_query(F.data == "ru")
async def set_lang(call: CallbackQuery, state: FSMContext, i18n: I18n):
    lang_code = "ru"
    await state.update_data(locale=lang_code)
    await call.answer(_("Язык изменён", locale=lang_code))
    await call.message.edit_text(_("Главное меню", locale=lang_code), reply_markup=mainm())


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(_("Выберите язык"), reply_markup=lang())


@dp.callback_query(F.data == "btmm")
async def back_to_main(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(_("Главное меню"), reply_markup=mainm())

@dp.callback_query((F.data == "rm") | (F.data == "btrm"))
async def catalogs_menu(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(_("Меню каталогов:"), reply_markup=catalogs())

@dp.callback_query(F.data == "salat")
async def show_salats(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(_("Салаты"), reply_markup=salats())

@dp.callback_query(F.data == "ff")
async def fast_food_menu(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(_("Все позиции фаст-фуда"), reply_markup=fast_food())

@dp.callback_query(F.data == "he")
async def hot_dishes(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(_("Горячие блюда"), reply_markup=hotd())

@dp.callback_query(F.data == "cs")
async def feedback_start(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer(_("Напишите сообщение, мы обязательно ответим"))
    await state.set_state(States.text)


@dp.message(States.text)
async def feedback_received(message: Message, state: FSMContext, bot: Bot):
    admin_id = getenv("ADMIN_ID")
    if admin_id:
        await bot.send_message(
            chat_id=admin_id,
            text=f"Новый отзыв от @{message.from_user.username}:\n\n{message.text}"
        )
    await message.answer(_("Ваше сообщение отправлено!"))
    data = await state.get_data()
    locale = data.get("locale")
    await state.clear()
    if locale:
        await state.update_data(locale=locale)




async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())