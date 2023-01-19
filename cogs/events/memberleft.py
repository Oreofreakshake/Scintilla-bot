async def memberleft(bot, message):
    leavingMember = message.left_chat_member.first_name
    await bot.send_message(message.chat.id, f"bye 👋 {leavingMember}")
