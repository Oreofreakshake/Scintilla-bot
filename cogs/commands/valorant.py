def extract_arg(arg):
    data = arg.split("/valorant ")[-1]
    return data


async def valorant(bot, message):
    riotID = extract_arg(message.text)
    if riotID[0] != "/":
        print(riotID)
    else:
        await bot.send_message(
            message.chat.id,
            "you need to give your riot username with tag\n(ex: /valorant SEN TenZ#0505)",
        )
        print("enter argument")
