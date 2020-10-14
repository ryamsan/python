import requests
page = requests.get("https://www.nea.gov.sg/weather")
print(page.content)
print(page.status_code)
print(page.raise_for_status())


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

four_day = soup.find(id='fourDayOutlook')
print(four_day)
#forecast_items = four_day.find_all(class_='content')


#print(forecast_items)

  
