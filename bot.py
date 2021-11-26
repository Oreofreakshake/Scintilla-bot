import os
import telebot
from dotenv import load_dotenv
import random


load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def welcome_text(message):
    bot.reply_to(message, "Hello, I'm working just fine!")


@bot.message_handler(commands=["saamometer"])
def saam_meter(message):
    tempINT = random.choice(range(101))
    value = str(tempINT)

    if tempINT > 90:
        bot.reply_to(message, "You are " + value + "% saam, damn unlucky")
    else:
        bot.reply_to(message, "You are " + value + "% saam")


if __name__ == "__main__":
    bot.infinity_polling()