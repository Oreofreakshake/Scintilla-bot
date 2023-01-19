from api.valorantAPI import GetAccount, GetRank


def extract_arg(arg):
    data = arg.split("/valorant ")[-1]
    return data


def ValidateAccout(username, tag):
    if len(tag) >= 2 and len(tag) <= 5:
        accountData = GetAccount(username, tag)
        region = accountData["data"]["region"]
        accountRank = GetRank(username, tag, region)

        rank = accountRank["data"]["currenttierpatched"]
        user = accountData["data"]["name"] + "#" + accountData["data"]["tag"]
        level = accountData["data"]["account_level"]
        userregion = accountData["data"]["region"]

        output = f"riot id: `{user}`\nlevel: `{level}`\nrank: `{rank}`\nregion: `{userregion}`"

        return output
    else:
        output = f"your tag is invalid, try again\n `/valorant`"
        return output


async def valorant(bot, message):
    riotIDarg = extract_arg(message.text)
    if riotIDarg[0] != "/":
        if "#" in riotIDarg:
            riotID = riotIDarg.split("#")
            username = riotID[0]
            tag = riotID[-1]

            DataGiven = ValidateAccout(username, tag)

            await bot.send_message(message.chat.id, DataGiven, parse_mode="MarkdownV2")
        else:
            await bot.send_message(message.chat.id, DataGiven, parse_mode="MarkdownV2")
    else:
        await bot.send_message(
            message.chat.id,
            "you need to give your riot username with tag\n(ex: /valorant SEN TenZ#0505)",
        )
        print("enter argument")
