import requests
from bs4 import BeautifulSoup

url = "https://www.nea.gov.sg/weather"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

four_day = soup.find(id = 'fourDayOutlook')
title = four_day.find('h2').get_text()
print(title)

day = soup.find(class_='content')
today = day.find('span').get_text()
print(today)
#today = day[0]
#print(today)











