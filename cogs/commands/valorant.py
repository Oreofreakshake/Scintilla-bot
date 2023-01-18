from api.valorantAPI import GetAccount, GetRank


def extract_arg(arg):
    data = arg.split("/valorant ")[-1]
    return data


async def valorant(bot, message):
    riotIDarg = extract_arg(message.text)
    if riotIDarg[0] != "/":
        if "#" in riotIDarg:
            riotID = riotIDarg.split("#")
            username = riotID[0]
            tag = riotID[-1]

            if len(tag) >= 2 and len(tag) <= 5:
                accountData = GetAccount(username, tag)
                region = accountData["data"]["region"]
                accountRank = GetRank(username, tag, region)

                rank = accountRank["data"]["currenttierpatched"]
                user = accountData["data"]["name"] + "#" + accountData["data"]["tag"]
                level = accountData["data"]["account_level"]
                userregion = accountData["data"]["region"]

                await bot.send_message(
                    message.chat.id,
                    f"riot ID: {user}\nlevel: {level}\nrank: {rank}\nregion: {userregion}",
                )
            else:
                await bot.send_message(
                    message.chat.id,
                    f"your tag is invalid as well, try again\n `/valorant`",
                    parse_mode="MarkdownV2",
                )

        else:
            await bot.send_message(
                message.chat.id,
                f"I need your tag, try again\n `/valorant`",
                parse_mode="MarkdownV2",
            )
    else:
        await bot.send_message(
            message.chat.id,
            "you need to give your riot username with tag\n(ex: /valorant SEN TenZ#0505)",
        )
        print("enter argument")
