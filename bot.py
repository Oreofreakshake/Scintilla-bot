import telebot
import asyncio
from telebot.async_telebot import AsyncTeleBot
import os
from dotenv import load_dotenv

load_dotenv()

# my lib
from cogs import cog__init__

from cogs import commandnames

# bot = telebot.TeleBot("TOKEN") before async
bot = AsyncTeleBot(os.getenv("TOKEN"))
name = commandnames
command = cog__init__.Commands(bot)





# setcommands
async def SetCommand():

    await bot.delete_my_commands(scope=None, language_code=None)

    Slash = []

    for item in range(len(name.commandsname)):
        Slash.append(
            telebot.types.BotCommand(
                name.commandsname[item], name.commanddescript[item]
            )
        )

    await bot.set_my_commands(commands=[Slash[0], Slash[1], Slash[2], Slash[3]])

    cmd = await bot.get_my_commands(scope=None, language_code=None)
    [c.to_json() for c in cmd]


# start command
@bot.message_handler(commands=["hello", "start"])  # ✅
async def start_command(message):
    await command.start_text(message)


# help command
@bot.message_handler(commands=["help"])
async def help_command(message):
    await command.help(message)


# out of context command
@bot.message_handler(commands=[name.commandsname[0]])  # ✅
async def command_one(message):
    await command.archive(message)


# prayer command
@bot.message_handler(
    commands=[name.commandsname[1]]
)  # ✅ (Will update and make it better later)
async def command_two(message):
    await command.prayertime(message)


@bot.message_handler(commands=[name.commandsname[2]])  # ✅
async def command_three(message):
    await command.getID(message)


# valorant command
@bot.message_handler(commands=[name.commandsname[3]])
async def command_four(message):
    await command.valorant(message)


# handler reply func
@bot.message_handler(content_types=["text"])
async def bot_reply_to_handler(message):
    if message.text == "save":
        await command.bot_reply_to_nocontext(message)
    if message.text == "Male'" or "Addu":
        await command.bot_reply_to_prayertime(message)




if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        print("I am online\n")
        asyncio.run(SetCommand())
        asyncio.run(bot.infinity_polling())
    except Exception as e:
        print("run time error\n", e)

# ==========================================================================================================================
