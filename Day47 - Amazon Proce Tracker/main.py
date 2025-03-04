#well use the https://de.camelcamelcamel.com/ to get amazon prices!

from bs4 import BeautifulSoup
import requests

url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup)

#We want to find: <span class="a-price-whole">…</span>

whole_price = soup.find('span', class_='a-price-whole')
fraction_price = soup.find('span', class_='a-price-fraction')

final_dollars = whole_price.getText().strip()
final_cents = fraction_price.getText().strip()

dollars = str(final_dollars)
cents = str(final_cents)

price = float(dollars) + (float(cents) / 100)

print(price)


