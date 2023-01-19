import requests


def GetAccount(username, tag):
    acc = f"https://api.henrikdev.xyz/valorant/v1/account/{username}/{tag}"
    json_data_acc = requests.get(acc).json()
    return json_data_acc


def GetRank(username, tag, region):
    rank = f"https://api.henrikdev.xyz/valorant/v1/mmr/{region}/{username}/{tag}"
    json_data_rank = requests.get(rank).json()
    return json_data_rank



print("Valorant cogs are ready!\n")
