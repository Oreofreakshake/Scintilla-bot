import telebot
import asyncio
from telebot.async_telebot import AsyncTeleBot

# my lib
from cogs import commands
from cogs import commandnames

# bot = telebot.TeleBot("5885503791:AAGP-d6F-eZZxB49gorKADSlDpnZATN60lg") before async
bot = AsyncTeleBot("5885503791:AAGP-d6F-eZZxB49gorKADSlDpnZATN60lg")
name = commandnames
command = commands.Commands(bot)

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

    await bot.set_my_commands(commands=[Slash[0], Slash[1], Slash[2]])


    cmd = await bot.get_my_commands(scope=None, language_code=None)
    [c.to_json() for c in cmd]


# start command
@bot.message_handler(commands=["hello", "start"])  # ✅
async def start_command(message):
    await command.welcome_text(message)


# out of context command
@bot.message_handler(commands=[name.commandsname[0]])  # ✅
async def command_one(message):
    await command.nocontext(message)


# prayer command
@bot.message_handler(
    commands=[name.commandsname[1]]
)  # ✅ (Will update and make it better later)
async def command_two(message):
    await command.prayertime(message)


@bot.message_handler(commands=[name.commandsname[2]])  # ✅
async def command_three(message):
    await command.getID(message)


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
