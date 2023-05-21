async def archive(bot, message):
    if message.chat.type != "private":
        await bot.send_message(message.chat.id, "You don't have permission to archive here")
    else:
        await bot.send_message(message.chat.id,'Reply "save" to archive the message\nArchives 👉 https://t.me/+AtmNJEY2dmQzYzRl',)


async def bot_reply_archive(bot, message):
    clipgroup = -934975694
    if message.chat.type == "private":
            if message.text == "save":
                    msgID = message.reply_to_message.message_id
                    await bot.send_message(message.chat.id, "archived")
            await bot.forward_message(clipgroup, message.chat.id, msgID)
    else:
        await bot.send_message(message.chat.id,  "You can't archive here")
