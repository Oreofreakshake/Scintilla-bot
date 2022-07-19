import telebot
from telebot.async_telebot import AsyncTeleBot

# my lib
from cogs import commands
from cogs import commandnames


# bot = telebot.TeleBot("5227265639:AAFAlErq_cl2QnS3MvDM7Fn_n2ZZ4U-g9hQ") before async
bot = AsyncTeleBot("5227265639:AAFAlErq_cl2QnS3MvDM7Fn_n2ZZ4U-g9hQ")
name = commandnames
command = commands.Commands(bot)

# setcommands
async def SetCommand():

    await bot.delete_my_commands(scope=None, language_code=None)

    await bot.set_my_commands(commands=[telebot.types.BotCommand(name.commandsname[0],name.commanddescript[0]),
    telebot.types.BotCommand(name.commandsname[1],name.commanddescript[1]),
    telebot.types.BotCommand(name.commandsname[2],name.commanddescript[2])
    ])

    cmd = await bot.get_my_commands(scope=None, language_code=None)
    [c.to_json() for c in cmd]


# start command
@bot.message_handler(commands=["hello", "start", "c"])  # ✅
async def start_command(message):
    await command.welcome_text(message)


# gayometer command
@bot.message_handler(commands=[name.commandsname[0]])  # ✅
async def command_one(message):
    await command.gay_meter(message)


# prayer command
@bot.message_handler(
    commands=[name.commandsname[1]]
)  # ✅ (Will update and make it better later)
async def command_two(message):
    await command.prayertime(message)


# covid command
@bot.message_handler(commands=[name.commandsname[2]])  # ✅
async def command_three(message):
    await command.covid(message)


# prayer command reply
@bot.message_handler(content_types=["text"])
async def bot_reply_to_island(message):
    await command.bot_reply_to_prayertime(message)


if __name__ == "__main__":
    try:
        import asyncio

        print("I am online\n")
        asyncio.run(SetCommand())
        asyncio.run(bot.infinity_polling())
    except:
        print("run time error\n")

# ==========================================================================================================================
# code i might need later
# def gen_markup(): ❌
#    markup = types.InlineKeyboardMarkup()
#    markup.row_width = 2
#    markup.add(
#        types.InlineKeyboardButton(text="something", callback_data="something"),
#    )
#    return markup
#
#
# @bot.callback_query_handler(func=lambda message: True)
# def callback_query(call):
#    if call.data == "something":
#        bot.answer_callback_query(call.id, text="You Clicked")
