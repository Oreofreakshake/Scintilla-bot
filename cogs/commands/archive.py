async def archive(bot, message):
        await bot.send_message(
            message.chat.id,
            'Reply "save" to archive the message',
        )

async def bot_reply_archive(bot, message):
    if message.text == "save":
        msgID = message.reply_to_message.message_id
        await bot.send_message(message.chat.id, "archived")
    await bot.forward_message(-803504766, message.chat.id, msgID)