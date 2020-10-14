import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.amazon.sg/Canon-EF-S18-135mm-3-5-5-6-Digital-Camera/dp/B01BUYJX6G/ref=sr_1_11?keywords=DSLR&qid=1588763242&s=gateway&sr=8-11'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

def check_price():

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id = "priceblock_ourprice").get_text().strip('S$').replace(',', '') # can't strip a comma
    converted_price = float(price[0:5])

    if(converted_price < 2000):
        send_mail()

    print(title.strip())
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ryanngoh123@gmail.com', 'kvwtokaodsphgvsg')
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.sg/Canon-EF-S18-135mm-3-5-5-6-Digital-Camera/dp/B01BUYJX6G/ref=sr_1_11?keywords=DSLR&qid=1588763242&s=gateway&sr=8-11'
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        'ryanngoh123@gmail.com',
        'ryanngohenrui@gmail.com',
        msg

    )
    print('Hey EMAIL has been sent!')

    server.quit()

check_price()
'''
while True:
    check_price()
    time.sleep(60 * 60)
'''
