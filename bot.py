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

    Slash = []
    n = 1  # to make it easier for you to read the list, just ignore 0 and start from 1

    for item in range(len(name.commandsname)):
        Slash.append(
            telebot.types.BotCommand(
                name.commandsname[item], name.commanddescript[item]
            )
        )

    await bot.set_my_commands(commands=[Slash[1 - n], Slash[2 - n]])

    cmd = await bot.get_my_commands(scope=None, language_code=None)
    [c.to_json() for c in cmd]


# start command
@bot.message_handler(commands=["hello", "start"])  # ✅
async def start_command(message):
    await command.welcome_text(message)


# prayer command
@bot.message_handler(
    commands=[name.commandsname[1]]
)  # ✅ (Will update and make it better later)
async def command_two(message):
    await command.prayertime(message)

# out of context command
@bot.message_handler(commands=[name.commandsname[0]])  # ❌
async def command_one(message):
    await command.nocontext(message)

# handler reply func
@bot.message_handler(content_types=["text"])
async def bot_reply_to_handler(message):
    if message.text == "save":
        await command.bot_reply_to_nocontext(message)
    if message.text == "Male'" or "Addu":
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
