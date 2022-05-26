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
        # Вытаскиваем наименование фильма
        for link in self.soup.find('____???____', '????'=re.compile('media-item-name')):
            if link.attrs['????'] is not None:
                self.film_name = link.attrs['????'']

        # Вытаскиваем дату релиза, продолжительность и возрастные ограничения фильма
        for link in soup.find_all('a', href=re.compile('^\/movies\?years=.*')):
            if link.attrs['href'] is not None:
                self.release_date = ((link.attrs['href']).split('=')[-1])
                # под этим же якорем
                self.duration = link.attrs['span']
                # под этим же якорем
                self.film_age_rating = link.attrs['span']

        # Вытаскиваем средний рейтинг фильма по версии Wink
        # На самом деле вытаскиваем только 1 цифру среднего рейтинга
        for link in soup.find_all('???', '????'=re.compile('rating_wink_int_part_r17g8ivt')):
            if link.attrs['href'] is not None:
                self.avr_grade = (link.attrs['????'])
        # Вытаскиваем описание фильма
        for link in soup.find('??', ???=re.compile('media-item-description$')):
            if link.attrs['????'] is not None:
                self.description = link.attrs['????']
        # Вытаскиваем жанр фильма
        for link in soup.find('a', href=re.compile('^movies\?vod_genres')):
            if link.attrs['href'] is not None:
                self.genre = link.attrs['href'].split('=')[0]
        # Вытаскиваем имя режиссера
        for link in soup.find('??', href=re.compile('root_r1ru04lg name_ntjejvp bold_bgok4v root_subtitle1_r18emsye')):
            if link.attrs['????'] is not None:
                    surname = link.attrs['????']
        for link in soup.find('????', href=re.compile('root_r1ru04lg name_ntjejvp root_subtitle2_rt60wi')):
            if link.attrs['????'] is not None:
                name = link.attrs['????']
        self.main_director = f'{surname} {name}'

        return self.id, self.film_name, self.release_date, self.duration, self.film_age_rating, self.link, self.main_director