from cogs import commandnames

n = 1  # to make it easier for you to read the list, just ignore 0 and start from 1


async def help(bot, message):
    await bot.send_message(
        message.chat.id,
        f"""𝗛𝗲𝗿𝗲 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝘆𝗼𝘂 𝗰𝗮𝗻 𝘂𝘀𝗲!
/{commandnames.commandsname[1-n]} - Use me to save your clips and messages
/{commandnames.commandsname[2-n]} - Use me for prayer timings in Male' and Addu
/{commandnames.commandsname[3-n]} - Use me to display current chat's ID
/{commandnames.commandsname[4-n]} - Use me as a valorant tracker
         """,
    )
