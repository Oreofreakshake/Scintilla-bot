import os
import telebot
from dotenv import load_dotenv
import logging

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)
logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=["start"])
def welcome_text(message):
    bot.reply_to(message, "Hello, I'm working just fine!")


if __name__ == "__main__":
    try:
        print("I am online")
        bot.infinity_polling()
    except:
        print("run time error")
