import os
import telebot
from cogs import commands


bot = telebot.TeleBot("5028843783:AAFQ8J-o1QQ8y2JFDGE2lOsxV4gpZpUU-7g")


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
