from telebot import types
from telebot.types import (
    InlineKeyboardMarkup,  # not use
    InlineKeyboardButton,  # not use
    ReplyKeyboardMarkup,  # not use
    ReplyKeyboardRemove,
    KeyboardButton,  # not use
)
from prettytable import PrettyTable
from datetime import datetime
import pytz

# my libraries
from api import prayerDB


async def prayertime(bot, message):  # ✅
    add_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Prayerbutton = ["Male'", "Addu"]
    buttons = []
    for items in Prayerbutton:
        button = types.KeyboardButton(items)
        buttons.append(button)
    # for index, button in enumerate(buttons):
    add_markup.add(buttons[0], buttons[1])
    await bot.send_message(
        message.chat.id,
        "For which location?",
        reply_markup=add_markup,
    )


async def bot_reply_to_prayertime(bot, message):

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

        await bot.send_message(
            message.chat.id,
            f"```{DataGivenM}```",
            reply_markup=ReplyKeyboardRemove(),
            parse_mode="Markdown",
        )
