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
    Fajar = FajarData.lower()  # fajar prayer time
    # print(Fajar)

# dhuhar data

lists = soup.find_all(
    "div",
    class_="dhuhar-tile",
)

for list in lists:
    DhuharData = list.find("span", class_="prayertime").text
    Dhuhar = DhuharData.lower()  # dhuhar prayer time
    # print(Dhuhar)

# asr data

lists = soup.find_all(
    "div",
    class_="asr-tile",
)

for list in lists:
    AsrData = list.find("span", class_="prayertime").text
    Asr = AsrData.lower()  # asr prayer time
    # print(Asr)

# maghrib data

lists = soup.find_all(
    "div",
    class_="maghrib-tile",
)

for list in lists:
    MaghribData = list.find("span", class_="prayertime").text
    Maghrib = MaghribData.lower()  # maghrib prayer time
    # print(Maghrib)

# isha data

lists = soup.find_all(
    "div",
    class_="isha-tile",
)

for list in lists:
    IshaData = list.find("span", class_="prayertime").text
    Isha = IshaData.lower()  # isha prayer time
    # print(Isha)


Currenttime = datetime.now().strftime("%H:%M %p").lower()  # current time
TodayData = date.today()  # todays date
