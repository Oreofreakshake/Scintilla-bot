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
    # -1001803564730 stapler out of context
    # -640047845 sigma out of context

    async def nocontext(self, message):
        await self.bot.send_message(
            message.chat.id,
            'Reply "save" to archive the message',
        )

    # -----------------------------------------------------------------------------------------------

    async def prayertime(self, message):  # ✅
        add_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        Prayerbutton = ["Male'", "Addu"]
        buttons = []

        for items in Prayerbutton:
            button = types.KeyboardButton(items)
            buttons.append(button)

        # for index, button in enumerate(buttons):
        add_markup.add(buttons[0], buttons[1])

        await self.bot.send_message(
            message.chat.id,
            "For which location?",
            reply_markup=add_markup,
        )

         # -----------------------------------------------------------------------------------------------

    async def getID(self, message):
        msgChatID = message.chat.id
        print(message)
        await self.bot.send_message(
            msgChatID,
            f"chat id : ```{msgChatID}```",
            reply_markup=ReplyKeyboardRemove(),
            parse_mode="Markdown",
        )

         # -----------------------------------------------------------------------------------------------

    async def bot_reply_to_nocontext(self, message):
        if message.text == "save":
            msgID = message.reply_to_message.message_id
            await self.bot.send_message(message.chat.id, "archived")

        await self.bot.forward_message(-1001650268553, message.chat.id, msgID)

         # -----------------------------------------------------------------------------------------------

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
