from api.valorantAPI import GetAccount, GetRank, GetBanner


def extract_arg(arg):
    data = arg.split("/valorant ")[-1]
    return data


def RegionDict(region):
    regions = {
        "ap": "Asia Pacific",
        "br": "Brazil",
        "eu": "Europe",
        "kr": "Korea",
        "latam": "Latin America",
        "na": "North America",
    }
    return regions[region]


def ValidateAccout(username, tag):
    if len(tag) >= 2 and len(tag) <= 5:

        auth = APIstatus(username, tag)

        if auth == 200:
            accountData = GetAccount(username, tag)
            region = accountData["data"]["region"]
            accountRank = GetRank(username, tag, region)

            rank = accountRank["data"]["currenttierpatched"]
            user = accountData["data"]["name"] + "#" + accountData["data"]["tag"]
            level = accountData["data"]["account_level"]
            userregionData = accountData["data"]["region"]
            userregion = RegionDict(userregionData)
            progress = accountRank["data"]["mmr_change_to_last_game"]

            output = f"`{user}`\n\n• Level: *{level}*\n• Rank: *{rank}*\n• Progress: *{progress}/100*\n• Region: *{userregion}*"
            return output

        elif auth == 404:
            output = "Player doesn't exist, sorry"
            return output
        elif auth == 403:
            output = "Server is under maintenance, try again later"
            return output
        elif auth == 408:
            output = "Timeout, try troubleshooting your internet"
            return output
        elif auth == 503:
            output = "Riot API seems to be down right now, try again later"
            return output
        elif auth == 429:
            output = "I'm being spammed right now, try again later"
            return output
        else:
            output = "I'm not really sure what's wrong 🤔"
            return output

    else:
        output = f"your tag is invalid, try again\n `/valorant`"
        return output


def APIstatus(username, tag):
    statusData = GetAccount(username, tag)
    status = statusData["status"]
    return status


async def valorant(bot, message):
    riotIDarg = extract_arg(message.text)
    if riotIDarg[0] != "/":
        if "#" in riotIDarg:
            riotID = riotIDarg.split("#")
            username = riotID[0]
            tag = riotID[-1]

            DataGiven = ValidateAccout(username, tag)

            auth = APIstatus(username, tag)

            if auth == 200:
                banner = GetBanner(username, tag)

                await bot.send_photo(
                    message.chat.id, banner, caption=DataGiven, parse_mode="MarkdownV2"
                )
            else:
                await bot.send_message(message.chat.id, DataGiven)

        else:
            await bot.send_message(
                message.chat.id,
                f"I need your tag, try again\n `/valorant`",
                parse_mode="MarkdownV2",
            )
    else:
        DataGiven = "you need to give your riot username with tag\n(ex: /valorant SEN TenZ#0505)"
        await bot.send_message(message.chat.id, DataGiven)
