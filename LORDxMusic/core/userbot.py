from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="LORDxAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="LORDxAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="LORDxAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="LORDxAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="LORDxAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER("مـيـوزك لـورد").info(f"جـار تـشـغـيـل الـحـسـاب الـمـسـاعـد")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("OOOJ30")
                await self.one.join_chat("M_4_M_C")
                await self.one.join_chat("M_R_ZC")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد .. بنجـاح ✅")
            except:
                LOGGER("مـيـوزك لـورد").error(
                    "حـدث خـطـاء اثـنـاء تـشـغـيـل الـحـسـاب الـمـسـاعـد تـاكـد انـك قـمـت بـأضـفـته لـجـروب الاشـعـارات ورفـعـه ادمـن...⁦♡"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER("مـيـوزك لـورد").info(f"تم بدء تشغيل الحساب المساعد {self.one.name} ...✓")

        if config.STRING2:
            await self.two.start()
            try:
                await self.one.join_chat("OOOJ30")
                await self.one.join_chat("M_4_M_C")
                await self.one.join_chat("M_R_ZC")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد² .. بنجـاح ✅")
            except:
                LOGGER(__name__).error(
                    "حـدث خـطـاء اثـنـاء تـشـغـيـل الـحـسـاب الـمـسـاعـد² تـاكـد انـك قـمـت بـأضـفـته لـجـروب الاشـعـارات ورفـعـه ادمـن...⁦♡"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER("مـيـوزك لـورد").info(f"تم بدء تشغيل الحساب المساعد² {self.one.name} ...✓")

        if config.STRING3:
            await self.three.start()
            try:
                await self.one.join_chat("OOOJ30")
                await self.one.join_chat("M_4_M_C")
                await self.one.join_chat("M_R_ZC")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد³ .. بنجـاح ✅")
            except:
                LOGGER("مـيـوزك لـورد").error(
                    "حـدث خـطـاء اثـنـاء تـشـغـيـل الـحـسـاب الـمـسـاعـد³ تـاكـد انـك قـمـت بـأضـفـته لـجـروب الاشـعـارات ورفـعـه ادمـن...⁦♡"
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER("مـيـوزك لـورد").info(f"تم بدء تشغيل الحساب المساعد³ {self.one.name} ...✓")

        if config.STRING4:
            await self.four.start()
            try:
                await self.one.join_chat("OOOJ30")
                await self.one.join_chat("M_4_M_C")
                await self.one.join_chat("M_R_ZC")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد⁴ .. بنجـاح ✅")
            except:
                LOGGER("مـيـوزك لـورد").error(
                    "حـدث خـطـاء اثـنـاء تـشـغـيـل الـحـسـاب الـمـسـاعـد⁴ تـاكـد انـك قـمـت بـأضـفـته لـجـروب الاشـعـارات ورفـعـه ادمـن...⁦♡"
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER("مـيـوزك لـورد").info(f"تم بدء تشغيل الحساب المساعد⁴ {self.one.name} ...✓")

        if config.STRING5:
            await self.five.start()
            try:
                await self.one.join_chat("OOOJ30")
                await self.one.join_chat("M_4_M_C")
                await self.one.join_chat("M_R_ZC")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "» تم تشغيـل الحسـاب المسـاعـد⅝ .. بنجـاح ✅")
            except:
                LOGGER("مـيـوزك لـورد").error(
                    "حـدث خـطـاء اثـنـاء تـشـغـيـل الـحـسـاب الـمـسـاعـد⅝ تـاكـد انـك قـمـت بـأضـفـته لـجـروب الاشـعـارات ورفـعـه ادمـن...⁦♡"
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER("مـيـوزك لـورد").info(f"تم بدء تشغيل الحساب المساعد⅝ {self.one.name} ...✓")

    async def stop(self):
        LOGGER(__name__).info(f"جـار ايـقـاف الـحـسـاب الـمـسـاعد...⁦♡")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
