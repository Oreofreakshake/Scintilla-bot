import telebot

# my lib
from cogs import commands
from api import prayer


bot = telebot.TeleBot("5028843783:AAFQ8J-o1QQ8y2JFDGE2lOsxV4gpZpUU-7g")


# start command
@bot.message_handler(commands=["hello", "start"])  # ✅
def start_command(message):
    command = commands.Commands(bot)
    command.welcome_text(message)


# saamometer command
@bot.message_handler(commands=["saamometer"])  # ✅
def command_one(message):
    command = commands.Commands(bot)
    command.saam_meter(message)


# prayer command
@bot.message_handler(commands=["prayertime"])  # ❌ (needs some fixing)
def command_two(message):
    command = commands.Commands(bot)
    command.prayertime(message)


@bot.message_handler(content_types=["text"])
def bot_reply_to_prayertime(message):
    command = commands.Commands(bot)
    command.bot_reply_to_prayertime(message)


if __name__ == "__main__":
    try:
        print("I am online")
        bot.infinity_polling()
    except:
        print("run time error")

# ==========================================================================================================================
# code i might need later
# def gen_markup():
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
