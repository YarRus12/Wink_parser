import requests
from urllib.request import urlopen
from urllib.response import addinfourl
import urllib
from bs4 import BeautifulSoup
import re
from fake_user_agent.main import user_agent

# В данном скрипте информация со списком страниц будет передаваться в Functional.films_pages
# И далее страницы с фильмами будут распарсеватсья на интересующие элементы, а именно

class page_parser:
    def __init__(self, page, headers):
        response = requests.get(page, headers=headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
            self.id = page.split('/')[-1]

class film_reaper(page_parser):
    def __init__(self):
        pass

    def reaper(self):
        for link in self.soup.find('____???____', '????'=re.compile('media-item-name')):
            if link.attrs['????'] is not None:
                self.film_name = link.attrs['????'']
        for link in soup.find_all('a', href=re.compile('^\/movies\?years=.*')):
            if link.attrs['href'] is not None:
                self.release_date = ((link.attrs['href']).split('=')[-1])
        for link in soup.find_all('???', '????'=re.compile('rating_wink_int_part_r17g8ivt')):
            if link.attrs['href'] is not None:
                self.avr_grade = (link.attrs['????'])
        for link in soup.find('??', ???=re.compile('media-item-description$')):
            if link.attrs['????'] is not None:
                self.description = link.attrs['????']

                href="/movies?vod_genres=49542078"


"""
`id`,
    `film_name`,
    `release_date`,
    `avr_grade`,
    `description`,
    `duration`,
    `link`,
    `main_director` """