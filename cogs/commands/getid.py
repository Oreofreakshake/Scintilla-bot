from telebot.types import (
    InlineKeyboardMarkup,  # not use
    InlineKeyboardButton,  # not use
    ReplyKeyboardMarkup,  # not use
    ReplyKeyboardRemove,
    KeyboardButton,  # not use
)



async def getID(bot, message):
    msgChatID = message.chat.id
    await bot.send_message(
        chat_id=msgChatID,
        text=f"chat id : ```{msgChatID}```",
        reply_markup=ReplyKeyboardRemove(),
        parse_mode="Markdown",
    )