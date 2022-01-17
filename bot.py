import os
from setuptools import Command
import telebot
from cogs import commands
from api import prayer

bot = telebot.TeleBot("5028843783:AAFQ8J-o1QQ8y2JFDGE2lOsxV4gpZpUU-7g")


@bot.message_handler(commands=["hello", "start"])  # ✅
def start_command(message):
    command = commands.Commands(bot)
    command.welcome_text(message)


@bot.message_handler(commands=["saamometer"])  # ✅
def command_one(message):
    command = commands.Commands(bot)
    command.saam_meter(message)


@bot.message_handler(commands=["prayertime"])  # ❌ (needs some fixing)
def command_two(message):
    command = commands.Commands(bot)
    command.prayertime(message)


if __name__ == "__main__":
    try:
        print("I am online")
        bot.infinity_polling()
    except:
        print("run time error")
