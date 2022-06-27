import os
import requests
from urllib.request import urlopen
from urllib.response import addinfourl
import urllib
from bs4 import BeautifulSoup
import re
from fake_user_agent.main import user_agent
import Links_extract
import Functional
import Media_parser
#import PyMySQL

DIR = os.path.dirname(os.path.abspath(__file__))
URL = 'https://wink.ru/media_items' #В качестве URL передаем ссылку на сайт онлайн кинотеатра Wink
#URL = https://www.kinopoisk.ru/lists/movies/?ss_subscription=ANY # Альтернатива это сайт kinopoisk
#Настраеваем липовый юзерагент для работы с защищенными сайтами
user_agent = user_agent("chrome")
#Передаем в переменную headers значения юзерагента
headers = {'accept': '*/*', 'user-agent': user_agent}

"""
ГОТОВЫЙ БЛОК 
"""
number_of_iter = 40 #Это число прокручиваний вниз для динамической страницы
for i in range(number_of_iter):
    #Поиск всех ссылок
    print(f'Начался поиск всех ссылок на странице "{URL}"')
    links = Links_extract.parse_pages(URL, headers)
    print('Началась выборка ссылок с фильмами из ссылок')
    film_links = Functional.films_pages(links, URL)
    #Проверка работоспособности ссылок
    print('Началась проверка работоспособности ссылок')
    film_links = Functional.working_check(film_links, headers)
    #Из ссылок с фильмами отбираются id
    print('Началась выборка id фильмов')
    film_links, id_list = Functional.id_separator(film_links)
    #Проверяем, если данные ссылки отсутвуют итоговом и соответствуют требованиям, то сохраняем в итоговый
    print('Началось включение id фильмов в результирующий список')
    Functional.result_list(DIR, id_list, film_links)
    print(f" Результирующий список включает в себя {len(set(open(DIR + '/result_list.txt').readlines()))} id")


films_url = 'https://wink.ru/media_items/'
with open(DIR + '/result_list.txt', 'r', encoding='utf-8') as f:
    for i in range(1):
        for i in f:
            films_info = Media_parser.page_parser(i, films_url, headers)
            print(films_info)
            films_info


a = 5
print(id(a))
a = str(a)
print(id(a))