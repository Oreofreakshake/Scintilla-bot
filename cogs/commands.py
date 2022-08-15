import random

from cogs import commandnames
from telebot import types
from telebot.types import (
    InlineKeyboardMarkup,  # not use
    InlineKeyboardButton,  # not use
    ReplyKeyboardMarkup,  # not use
    ReplyKeyboardRemove,
    KeyboardButton,  # not use
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

    async def welcome_text(self, message):  # ✅
        await self.bot.send_message(
            message.chat.id,
            f"""These are the commands you can try for now! 
/{commandnames.commandsname[1-n]} 
/{commandnames.commandsname[2-n]}
/{commandnames.commandsname[3-n]} 
         """,
        )

    # -----------------------------------------------------------------------------------------------

    async def gay_meter(self, message):  # ✅
        tempINT = random.choice(range(101))
        value = str(tempINT)
        if tempINT > 90:
            await self.bot.reply_to(message, "You are " + value + "% gay, damn unlucky")
        else:
            await self.bot.reply_to(message, "You are " + value + "% gay")

    # -----------------------------------------------------------------------------------------------

    async def prayertime(self, message):  # ✅
        add_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        Prayerbutton = ["Male'", "Addu"]
        buttons = []

        for items in Prayerbutton:
            button = types.KeyboardButton(items)
            buttons.append(button)

        for button in buttons:
            add_markup.add(button)

        await self.bot.send_message(
            message.chat.id,
            "For which location?",
            reply_markup=add_markup,
        )

    async def bot_reply_to_prayertime(self, message):

        timeinmv = pytz.timezone("Indian/Maldives")

        timer = datetime.now(timeinmv).strftime("%H:%M").lower()

        CurrentTime = f"{timer}"

        iterateList = ["Fajuru", "Dhuhr", "Asr", "Maghrib", "Isha"]

        day = prayerDB.get_day()
        catID = prayerDB.getIsland(message)

        # --------driver code---------

        if message.text == message.text:
            prayerTimes = prayerDB.getPrayerTime(catID, day)

            timeArray = []
            for time in iterateList:
                timeArray.append(prayerTimes[time])

            DataGivenM = PrettyTable(["Prayer", f"Time ({message.text})"])

            for row in range(len(iterateList)):
                DataGivenM.add_row([iterateList[row], timeArray[row]])

            await self.bot.send_message(
                message.chat.id,
                f"```{DataGivenM}```",
                reply_markup=ReplyKeyboardRemove(),
                parse_mode="Markdown",
            )

    # -----------------------------------------------------------------------------------------------

    async def covid(self, message):
        data = f"""*This data is only valid in Maldives*\n
Total Cases : ```{corona.totalCases}```
Total Deaths : ```{corona.totalDeaths}```
Active : ```{corona.active}```
Recovered : ```{corona.recovered}```
Critical : ```{corona.critical}```
        """

        await self.bot.send_message(message.chat.id, f"{data}", parse_mode="Markdown")
