import requests
from bs4 import BeautifulSoup

#my bd: 1990-09-11
#Marias bd = 1997-03-27

date = input('what year you would like to travel to? use YYY-MM-DD format\n')
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


#We are tring to get this:
#<h3 id="title-of-a-story" class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 
# lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max 
# a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"> Not Like Us </h3>

url = 'https://www.billboard.com/charts/hot-100/' + date

response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

titles = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in titles]
print(song_names)