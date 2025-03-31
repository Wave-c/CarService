from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

class MainKeyboard(ReplyKeyboardMarkup):
    def __init__(self):
        builder = ReplyKeyboardBuilder()
        builder.button("Записаться")
        builder.button("")