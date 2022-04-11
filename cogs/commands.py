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
from api import prayerDB
from api import corona

from prettytable import PrettyTable

from datetime import datetime, date
import pytz


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
/{commandnames.commandsname[3-n]} 
         """,
        )

    # -----------------------------------------------------------------------------------------------

    def saam_meter(self, message):  # ✅
        tempINT = random.choice(range(101))
        value = str(tempINT)
        if tempINT > 90:
            self.bot.reply_to(message, "You are " + value + "% saam, damn unlucky")
        else:
            self.bot.reply_to(message, "You are " + value + "% saam")

    # -----------------------------------------------------------------------------------------------

    def prayertime(self, message):  # ✅ 
        add_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        Prayerbutton = ["Fajuru", "Dhuhr", "Asr", "Maghrib", "Isha", "Every prayer"]
        buttonArray = []

        for items in range(len(Prayerbutton)):
            button = types.KeyboardButton(Prayerbutton[items])
            buttonArray.append(button)

        add_markup.add(buttonArray[0],buttonArray[1],buttonArray[2],buttonArray[3],buttonArray[4],buttonArray[5])

        self.bot.send_message(
            message.chat.id,
            "What prayer time do you want to know?",
            reply_markup=add_markup,
        )

    def bot_reply_to_prayertime(self, message):

        timeinmv = pytz.timezone("Indian/Maldives")

        Currenttime = datetime.now(timeinmv).strftime("%H:%M").lower()

        
        

        














































    # -----------------------------------------------------------------------------------------------

    def covid(self, message):
        data = f"""*This data is only valid in Maldives*\n
Total Cases : ```{corona.totalCases}```
Total Deaths : ```{corona.totalDeaths}```
Today Cases : ```{corona.todayCases}```
Today Deaths : ```{corona.todayDeaths}```
Active : ```{corona.active}```
Recovered : ```{corona.recovered}```
Critical : ```{corona.critical}```
        """

        self.bot.send_message(message.chat.id, f"{data}", parse_mode="Markdown")
