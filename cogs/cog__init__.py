# my libraries
# commands
from cogs.commands.prayertime import prayertime, bot_reply_to_prayertime
from cogs.commands.archive import archive, bot_reply_archive
from cogs.commands.getid import getID
from cogs.commands.valorant import valorant
from cogs.commands.help import help



class Commands:
    def __init__(self, bot):
        self.bot = bot

    async def start_text(self, message):  # ✅
        await self.bot.send_message(
            message.chat.id,
            f"""Hello 👋\nYou can use /help for every command details""",
        )

    # -----------------------------------------------------------------------------------------------

    async def help(self, message):
        await help(self.bot, message)

    async def archive(self, message):
        await archive(self.bot, message)

    # -----------------------------------------------------------------------------------------------

    async def prayertime(self, message):  # ✅
        await prayertime(self.bot, message)

        # -----------------------------------------------------------------------------------------------

    async def getID(self, message):
        await getID(self.bot, message)

    async def valorant(self, message):
        await valorant(self.bot, message)

        # -----------------------------------------------------------------------------------------------

    async def bot_reply_to_nocontext(self, message):
        await bot_reply_archive(self.bot, message)

        # -----------------------------------------------------------------------------------------------

    async def bot_reply_to_prayertime(self, message):
        await bot_reply_to_prayertime(self.bot, message)

    # -----------------------------------------------------------------------------------------------

print("Commands successfully initialized!\n")