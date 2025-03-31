#well use the https://de.camelcamelcamel.com/ to get amazon prices!

from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()   #take environmental variables from .env

MY_PASS  = os.environ["MY_PASS"]
MY_EMAIL  = os.environ["SMPT_EMAIL"]

HEADERS = {"Accept-Language": "en-US",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

url = "https://www.amazon.de/-/en/gp/product/B091B1PXV8/ref=ox_sc_act_title_1?smid=A7207XU86IMSS&th=1"
# This is a test link: "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=url, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())

#We want to find: <span class="a-price-whole">…</span>

whole_price = soup.find('span', class_='a-price-whole')
print(whole_price)
fraction_price = soup.find('span', class_='a-price-fraction')
print(fraction_price)

final_dollars = whole_price.getText().strip()
final_cents = fraction_price.getText().strip()

dollars = str(final_dollars)
cents = str(final_cents)

price = float(dollars) + (float(cents) / 100)

print(price)


if price > 70:
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)   #you can directly use os.environ["X"]
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="lgzg90@hotmail.com", #irl use row['email']
                            msg=f"Subject:Low Price\n\nYout item is in a good price, buy now! go to {url}")

