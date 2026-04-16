from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
# Импортируем gettext для перевода кнопок
from aiogram.utils.i18n import gettext as _

def mainm():
    markup = InlineKeyboardBuilder()
    markup.add(
        InlineKeyboardButton(text=_("Меню каталогов"), callback_data="rm"),
        InlineKeyboardButton(text=_("Связаться с нами"), callback_data="cs")
    )
    markup.adjust(1)
    return markup.as_markup()

def lang():
    markup = InlineKeyboardBuilder()
    markup.add(
        InlineKeyboardButton(text="Uz 🇺🇿", callback_data="uz"),
        InlineKeyboardButton(text="En 🇺🇸", callback_data="en"),
        InlineKeyboardButton(text="Ru 🇷🇺", callback_data="ru")
    )
    markup.adjust(1)
    return markup.as_markup()

def catalogs():
    markup = InlineKeyboardBuilder()
    markup.add(
        InlineKeyboardButton(text=_("Салаты"), callback_data="salat"),
        InlineKeyboardButton(text=_("Фаст-фуд"), callback_data="ff"),
        InlineKeyboardButton(text=_("Горячие блюда"), callback_data="he"),
        InlineKeyboardButton(text=_("Назад"), callback_data="btmm")
    )
    markup.adjust(1)
    return markup.as_markup()

def salats():
    markup = InlineKeyboardBuilder()
    markup.add(
        InlineKeyboardButton(text=_("Цезарь"), callback_data="1s"),
        InlineKeyboardButton(text=_("Оливье"), callback_data="2s"),
        InlineKeyboardButton(text=_("Назад"), callback_data="btrm")
    )
    markup.adjust(1)
    return markup.as_markup()

def fast_food():
    markup = InlineKeyboardBuilder()
    markup.add(
        InlineKeyboardButton(text=_("Бургер"), callback_data="1f"),
        InlineKeyboardButton(text=_("Хот-дог"), callback_data="2f"),
        InlineKeyboardButton(text=_("Назад"), callback_data="btrm")
    )
    markup.adjust(1)
    return markup.as_markup()

def hotd():
    markup = InlineKeyboardBuilder()
    markup.add(
        InlineKeyboardButton(text=_("Плов"), callback_data="1h"),
        InlineKeyboardButton(text=_("Суп"), callback_data="2h"),
        InlineKeyboardButton(text=_("Назад"), callback_data="btrm")
    )
    markup.adjust(1)
    return markup.as_markup()
