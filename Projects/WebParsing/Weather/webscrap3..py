import requests
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
# print(forecast_items) give us a list of Today til Thursday
today = forecast_items[0]
#print(today.prettify())
 # we want Today
 # we want description of condition title property of img
 # we want short desc of conditions
 # the low temp

period = today.find(class_="period-name")
print(period.get_text())
short_desc = today.find(class_="short-desc")
print(short_desc.get_text())
temp = today.find(class_="temp")
print(temp.get_text())
#now find img desc
img = today.find("img")
print(img)
print(type(img))
desc = img['alt']
print(desc)





period_tag = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tag]
import pprint
pprint.pprint(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d['title'] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(desc)

import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "descs":descs
})

print(weather) 
