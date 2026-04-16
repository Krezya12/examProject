from aiogram.types import KeyboardButton, Message, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def mainm():
    markup = InlineKeyboardBuilder()
    markup.add(*[
        InlineKeyboardButton(text="Меню ресторана", callback_data="rm"),
        InlineKeyboardButton(text="Связаться с нами", callback_data="cs")
    ])
    markup.adjust(1, 1)
    markup.as_markup(resize_keyboard=True)
    return markup.as_markup()

def lang():
    markup = InlineKeyboardBuilder()
    markup.add(*[
        InlineKeyboardButton(text="🇺🇿 Uz", callback_data="uz"),
        InlineKeyboardButton(text="🇺🇸 En", callback_data="en")
    ])
    markup.adjust(1, 1)
    markup.as_markup(resize_keyboard=True)
    return markup.as_markup()

def catalogs():
    markup = InlineKeyboardBuilder()
    markup.add(*[
        InlineKeyboardButton(text="Салаты", callback_data="salat"),
        InlineKeyboardButton(text="Еда быстрого приготовления", callback_data="ff"),
        InlineKeyboardButton(text="Горячие блюда", callback_data="he"),
        InlineKeyboardButton(text="Назад", callback_data="btmm")
    ])
    markup.adjust(1, 1)
    markup.as_markup(resize_keyboard=True)
    return markup.as_markup()

def salats():
    markup = InlineKeyboardBuilder()
    markup.add(*[
        InlineKeyboardButton(text="Оливье", callback_data="1s"),
        InlineKeyboardButton(text="Цезарь", callback_data="2s"),
        InlineKeyboardButton(text="Назад", callback_data="btrm")
    ])
    markup.adjust(1, repeat=True)
    markup.as_markup(resize_keyboard=True)
    return markup.as_markup()

def fast_food():
    markup = InlineKeyboardBuilder()
    markup.add(*[
        InlineKeyboardButton(text="Бургер", callback_data="1f"),
        InlineKeyboardButton(text="Шаурма", callback_data="2f"),
        InlineKeyboardButton(text="Назад", callback_data="btrm")
    ])
    markup.adjust(1, repeat=True)
    markup.as_markup(resize_keyboard=True)
    return markup.as_markup()

def hotd():
    markup = InlineKeyboardBuilder()
    markup.add(*[
        InlineKeyboardButton(text="Плов", callback_data="1h"),
        InlineKeyboardButton(text="Суп", callback_data="2h"),
        InlineKeyboardButton(text="Назад", callback_data="btrm")
    ])
    markup.adjust(1, repeat=True)
    markup.as_markup(resize_keyboard=True)
    return markup.as_markup()