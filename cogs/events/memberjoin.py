import random


async def memberjoin(bot, message):
    newMember = message.new_chat_members[0].first_name

    responses = [
        f"Hope you bought some pizza 😁 {newMember} Welcome!",
        f"Good morning {newMember} or night... I'm not really sure",
        f"Potential player to replace our viper main, Welcome {newMember}!",
        f"Do you believe in being redpilled? nvm don't answer that, Welcome {newMember}!",
        f"I'm the best player in this team btw, you stay safe tho 🙏 {newMember}",
        f"CROSSHAIR PLACEMENT!!! useles- oh hello {newMember} don't mind us",
        f"Listening to spotify rn 🎵 show me your most played album {newMember} 😁",
    ]
    response = random.choice(responses)

    await bot.send_message(message.chat.id, response)
