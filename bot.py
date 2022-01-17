import os
import telebot
from dotenv import load_dotenv
from cogs import commands


load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_command(message):
    command = commands.Commands(bot)
    command.welcome_text(message)


@bot.message_handler(commands=["saamometer"])
def command_one(message):
    command = commands.Commands(bot)
    command.saam_meter(message)


if __name__ == "__main__":
    try:
        print("I am online")
        bot.infinity_polling()
    except:
        print("run time error")
