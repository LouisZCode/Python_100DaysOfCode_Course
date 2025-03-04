from bs4 import BeautifulSoup
import requests

#But how do we scrape a live website?
# lets try with:   https://news.ycombinator.com/news

#to get the data we will use requests
response = requests.get('https://news.ycombinator.com/news')
hacker_webpage = response.text

#we just got the code!! its just html...

#it is an anchor tag!! 
#what if I want the title of the post with more "likes", well, first lets inspect a title: 
#<a href="https://www.keelinglabs.com/jobs">Keeling Labs (YC W23) Is Hiring an ML Engineer for Climate Tech (Los Angeles)</a>

#and what about the points? the likse... lets see..
#<span class="score" id="score_43243914">80 points</span>

"""lets get all the titles and all the points, and after, compare all of them to see which one has the highes points!"""

soup = BeautifulSoup(hacker_webpage, "html.parser")
article_text = soup.find(name='a', class_="storylink")

print(article_text.get_text())

