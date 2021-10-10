import telebot

bot = telebot.TeleBot("token", parse_mode=None)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "saam is gay, i'm just testing the API")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()