from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url='https://youtu.be/xyz'),
            InlineKeyboardButton(text="Telegram", url='tg://resolve?domain=xyz')
        ]
    ]
)