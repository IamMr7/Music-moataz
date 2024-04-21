from pyrogram import filters
from pyrogram.types import Message

from LORDxMusic import app
from LORDxMusic.core.call import LORDy
from LORDxMusic.utils.database import is_music_playing, music_off
from LORDxMusic.utils.decorators import AdminRightsCheck
from LORDxMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["اوقف"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await LORDy.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
