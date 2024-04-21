from pyrogram.types import InlineKeyboardButton

import config
from LORDxMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["LORD_BUTTON3"],
                url=f"https://t.me/vx_fs",
            )
        ],
        [
            InlineKeyboardButton(text=_["LORD_BUTTON"], url="https://t.me/S_O_M_A44"),
            InlineKeyboardButton(text=_["LORD_BUTTON2"], url="https://t.me/M2RR1"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_1"], url="https://t.me/{app.username}?startgroup=true"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["LORD_BUTTON3"],
                url=f"https://t.me/vx_fs",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["LORD_BUTTON"], url="https://t.me/S_O_M_A44"),
            InlineKeyboardButton(text=_["LORD_BUTTON2"], url="https://t.me/M2RR1"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_1"], url="https://t.me/{app.username}?startgroup=true"),
        ],
    ]
    return buttons
