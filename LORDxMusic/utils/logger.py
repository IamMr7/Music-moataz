from pyrogram.enums import ParseMode

from LORDxMusic import app
from LORDxMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>━━━━━✯ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗟𝗼𝗿𝗱 ✯━━━━━<b>
<b>𝅄 𓏺 𝖦𝗋𝗈𝗎𝗉 :<b> {message.chat.title}
<b>━━━━━━━━━━━━━━━<b> 
<b>𝅄 𓏺 𝖦𝗋𝗈𝗎𝗉 𝖨𝖣 :<b> <code>[{message.chat.id}]</code>
<b>━━━━━━━━━━━━━━━<b>
<b>𝅄 𓏺 𝖭𝖺𝗆𝖾 :<b> › {message.from_user.mention}
<b>━━━━━━━━━━━━━━━<b>
<b>𝅄 𓏺 𝖴𝗌𝖾𝗋 𝖭𝖺𝗆𝖾 :<b> › @{message.from_user.username}
<b>━━━━━━━━━━━━━━━<b>
<b>𝅄 𓏺 𝖴𝗌𝖾𝗋 𝖨𝖣 :<b> › <code>{message.from_user.id}</code>
<b>━━━━━━━━━━━━━━━<b>
<b>𝅄 𓏺 𝖴𝗌𝖾𝗋 𝖦𝗋𝗈𝗎𝗉 :<b> > @{message.chat.username}
<b>━━━━━━━━━━━━━━━<b>
<b>𝅄 𓏺 𝖯𝗅𝖺𝗒𝗂𝗇𝗀 𝖭𝗈𝗐 :<b> {message.text.split(None, 1)[1]}
<b>━━━━━━━━━━━━━━━<b>
<b>𝅄 𓏺 𝖲𝗍𝗋𝖾𝖺𝗆𝗂𝗇𝗀 :<b> {streamtype}
<b>━━━━━━━━━━━━━━━<b>"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
