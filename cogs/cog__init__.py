# my libraries
from cogs import commandnames

# bot commands

from cogs.commands.prayertime import prayertime, bot_reply_to_prayertime
from cogs.commands.archive import archive, bot_reply_archive
from cogs.commands.getid import getID

n = 1  # to make it easier for you to read the list, just ignore 0 and start from 1


class Commands:
    def __init__(self, bot):
        self.bot = bot

    async def start_text(self, message):  # ✅
        await self.bot.send_message(
            message.chat.id,
            f"""These are the commands you can try for now!
/{commandnames.commandsname[1-n]}
/{commandnames.commandsname[2-n]}
/{commandnames.commandsname[3-n]} 
         """,
        )

    # -----------------------------------------------------------------------------------------------

    async def archive(self, message):
        await archive(self.bot, message)

    # -----------------------------------------------------------------------------------------------

    async def prayertime(self, message):  # ✅
        await prayertime(self.bot, message)
        
        # -----------------------------------------------------------------------------------------------

    async def getID(self, message):
        await getID(self.bot, message)

        # -----------------------------------------------------------------------------------------------

    async def bot_reply_to_nocontext(self, message):
        await bot_reply_archive(self.bot, message)

        # -----------------------------------------------------------------------------------------------

    async def bot_reply_to_prayertime(self, message):
        await bot_reply_to_prayertime(self.bot, message)



    # -----------------------------------------------------------------------------------------------
