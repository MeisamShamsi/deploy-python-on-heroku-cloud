import requests
from bs4 import BeautifulSoup
import time
import datetime


TOKEN = "6237163602:AAExRUCdv9r0CEPXGagRkiGu_St9AOikHQ8"
CHAT_ID = "-1001714864695"

def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": "-1001714864695", "text": message}
    response = requests.post(url, data=data)
    return response.json()

while True:
    # Check if the current day is a weekend (Saturday or Sunday)
    current_day = datetime.datetime.now().weekday()
    if current_day >= 5:
        # If it is a weekend, wait until Monday to continue
        next_weekday = (7 - current_day) % 7
        wait_time = datetime.timedelta(days=next_weekday)
        # Use this website for Emoji: https://unicode.org/emoji/charts/full-emoji-list.html
        # Replace + with 000
        message = "Happy Weekend \U0001F600"
        send_message_to_telegram(message)
        time.sleep(wait_time.total_seconds())
    else:
        # If it is a weekday, retrieve the oil price and send it to Telegram
        url = "https://www.marketwatch.com/investing/future/cl.1"
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        # find all paragraphs with class "text"
        oil_price = soup.find("span", class_="value").text

        message = f"Live price of WTI USOIL is: ${oil_price}"
        send_message_to_telegram(message)

        # Wait for 5 minutes before repeating the loop
        time.sleep(300)