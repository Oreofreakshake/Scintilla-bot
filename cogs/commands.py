import random

from cogs import commandnames
from telebot import types
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
)
from api import prayer
from datetime import date, datetime

n = 1  # to make it easier for you to read the list, just ignore 0 and start from 1


class Commands:
    def __init__(self, bot):
        self.bot = bot

    def welcome_text(self, message):  # ✅
        self.bot.send_message(
            message.chat.id,
            f"""These are the commands you can try for now! 
/{commandnames.commandsname[1-n]} 
/{commandnames.commandsname[2-n]} 
         """,
        )

    def saam_meter(self, message):  # ✅
        tempINT = random.choice(range(101))
        value = str(tempINT)
        if tempINT > 90:
            self.bot.reply_to(message, "You are " + value + "% saam, damn unlucky")
        else:
            self.bot.reply_to(message, "You are " + value + "% saam")

    def prayertime(self, message):  # ❌ (still need some work)
        add_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Fajar")
        button2 = types.KeyboardButton("Dhuhar")
        button3 = types.KeyboardButton("Asr")
        button4 = types.KeyboardButton("Maghrib")
        button5 = types.KeyboardButton("Isha")
        button6 = types.KeyboardButton("All")
        add_markup.add(button1, button2, button3, button3, button4, button5, button6)
        self.bot.send_message(
            message.chat.id,
            "What prayer time do you want to know?",
            reply_markup=add_markup,
        )

    def bot_reply_to_prayertime(self, message):
        Fajar = prayer.Fajar
        Dhuhar = prayer.Dhuhar
        Asr = prayer.Asr
        Maghrib = prayer.Maghrib
        Isha = prayer.Isha

        if message.text == "Fajar":
            self.bot.reply_to(message, Fajar, reply_markup=ReplyKeyboardRemove())
        if message.text == "Dhuhar":
            self.bot.reply_to(message, Dhuhar, reply_markup=ReplyKeyboardRemove())
        if message.text == "Asr":
            self.bot.reply_to(message, Asr, reply_markup=ReplyKeyboardRemove())
        if message.text == "Maghrib":
            self.bot.reply_to(message, Maghrib, reply_markup=ReplyKeyboardRemove())
        if message.text == "Isha":
            self.bot.reply_to(message, Isha, reply_markup=ReplyKeyboardRemove())
        if message.text == "All":
            self.bot.reply_to(message, "-", reply_markup=ReplyKeyboardRemove())
