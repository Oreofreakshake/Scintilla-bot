import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
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
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("fathis", callback_data="cb_fathis"),
        InlineKeyboardButton("dhuhar", callback_data="cb_dhuhar"),
        InlineKeyboardButton("asr", callback_data="cb_asr"),
        InlineKeyboardButton("maghrib", callback_data="cb_maghrib"),
        InlineKeyboardButton("isha", callback_data="cb_isha"),
        InlineKeyboardButton("all", callback_data="cb_all"),
    )
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")


@bot.message_handler(func=lambda message: True)  # ❌ (needs some fixing)
def command_two(message):
    bot.send_message(
        message.chat.id,
        "Which prayer time are you looking for?",
        reply_markup=gen_markup(),
    )
    # command = commands.Commands(bot)
    # command.prayertime(message)


if __name__ == "__main__":
    try:
        print("I am online")
        bot.infinity_polling()
    except:
        print("run time error")
