from bs4 import BeautifulSoup
import requests
from datetime import datetime, date

url = "https://www.islamicfinder.org/world/maldives/1282027/male-prayer-times/"

session = requests.get(url)

soup = BeautifulSoup(session.content, "html.parser")


# fajar data

lists = soup.find_all(
    "div",
    class_="fajar-tile",
)

for list in lists:
    FajarData = list.find("span", class_="prayertime").text
    Fajar12hour = FajarData.lower()  # fajar prayer time -------------------------
    # print(Fajar)

# dhuhar data

lists = soup.find_all(
    "div",
    class_="dhuhar-tile",
)

for list in lists:
    DhuharData = list.find("span", class_="prayertime").text
    Dhuhar12hour = DhuharData.lower()  # dhuhar prayer time --------------------------
    # print(Dhuhar)

# asr data

lists = soup.find_all(
    "div",
    class_="asr-tile",
)

for list in lists:
    AsrData = list.find("span", class_="prayertime").text
    Asr12hour = AsrData.lower()  # asr prayer time -------------------------
    # print(Asr)

# maghrib data

lists = soup.find_all(
    "div",
    class_="maghrib-tile",
)

for list in lists:
    MaghribData = list.find("span", class_="prayertime").text
    Maghrib12hour = MaghribData.lower()  # maghrib prayer time -------------------------
    # print(Maghrib)

# isha data

lists = soup.find_all(
    "div",
    class_="isha-tile",
)

for list in lists:
    IshaData = list.find("span", class_="prayertime").text
    Isha12hour = IshaData.lower()  # isha prayer time ------------------------------
    # print(Isha)


Currenttime12hour = datetime.now().strftime("%H:%M %p").lower()  # current time
TodayData = date.today()  # todays date


def convert24(str1):
    if str1[-2:] == "am" and str1[:2] == "12":
        return "00" + str1[2:-2]

    elif str1[-2:] == "am":
        return str1[:-2]

    elif str1[-2:] == "pm" and str1[:2] == "12":
        return str1[:-2]

    else:
        return str(int(str1[:2]) + 12) + str1[2:5]


# converting to 24hours
Fajar = convert24(Fajar12hour)
Dhuhar = convert24(Dhuhar12hour)
Asr = convert24(Asr12hour)
Maghrib = convert24(Maghrib12hour)
Isha = convert24(Isha12hour)
Currenttime = convert24(Currenttime12hour)
# ----------------------------------------------------------------------------------------
ListOfTimeLeft = []

# getting the time difference
TimeLeftFajar = int(Currenttime[:2]) - int(Fajar[:2])
TimeLeftDhuhar = int(Currenttime[:2]) - int(Dhuhar[:2])
TimeLeftAsr = int(Currenttime[:2]) - int(Asr[:2])
TimeLeftMaghrib = int(Currenttime[:2]) - int(Maghrib[:2])
TimeLeftIsha = int(Currenttime[:2]) - int(Isha[:2])

ListOfTimeLeft.append(TimeLeftFajar)
ListOfTimeLeft.append(TimeLeftDhuhar)
ListOfTimeLeft.append(TimeLeftAsr)
ListOfTimeLeft.append(TimeLeftMaghrib)
ListOfTimeLeft.append(TimeLeftIsha)

hourDiff = []

# removing the negs
for time in ListOfTimeLeft:
    if time < 0:
        time = -time
        hourDiff.append(time)

# ----------------------------------------------------------------------------------------
# final time difference
TimeLeftFajar = hourDiff[0]
TimeLeftDhuhar = hourDiff[1]
TimeLeftAsr = hourDiff[2]
TimeLeftMaghrib = hourDiff[3]
TimeLeftIsha = hourDiff[4]
