#lets webscarpe this page and make a txt file from it:
# https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

from bs4 import BeautifulSoup
import requests

movie_page = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(movie_page.text, 'html.parser')

all_titles_html = soup.find_all('h3')

movie_titles = [movies.getText() for movies in all_titles_html]  #We get the lis from 100 - 1!
movies = movie_titles[::-1] #this takes the list and makes it in reverse... so from 1 - 100

with open('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")
        