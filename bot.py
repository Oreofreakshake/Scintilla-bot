import os
import telebot
from dotenv import load_dotenv
from cogs import commands


load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def welcome_text(message):
    bot.reply_to(message, "Hello, I'm working just fine!")


@bot.message_handler(commands=["saamometer"])
def command_one(message):
    value = commands.Commands(bot)
    value.saam_meter(message)


if __name__ == "__main__":
    try:
        print("I am online")
        bot.infinity_polling()
    except:
        print("run time error")
