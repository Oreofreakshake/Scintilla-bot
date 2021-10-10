import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    textList = [
        "Hello i'm online, type /help to get the bot commands, I'll add the saam commands later"
    ]
    bot.send_message(text=textList[0], chat_id=-1001467819274)


@bot.message_handler(commands=["help"])
def send_welcome(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Message the developer", url="telegram.me/zuccccc"
        )
    )
    bot.send_message(
        chat_id=-1001467819274,
        text="- /start to check if the bot is online\n- /('anything you want') to echo whatever you say\n",
        reply_markup=keyboard,
    )


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()