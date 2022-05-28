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
#import Media_parser
#import PyMySQL

DIR = os.path.dirname(os.path.abspath(__file__))
#В качестве URL передаем ссылку на сайт онлайн кинотеатра Wink
URL = 'https://wink.ru/media_items'
#Настраеваем липовый юзерагент для работы с защищенными сайтами
user_agent = user_agent("chrome")
#Передаем в переменную headers значения юзерагента
headers = {'accept': '*/*', 'user-agent': user_agent}

number_of_iter = 10
for i in range(number_of_iter):
    #Поиск всех ссылок
    print(f'Начался поиск всех ссылок на странице "{URL}"')
    links = Links_extract.parse_pages(URL, headers)
    #Проверка работоспособности ссылок
    print('Началась проверка работоспособности ссылок')
    working_links = Functional.working_check(links, headers)
    print('Началась выборка ссылок с фильмами из работоспособных ссылок')
    film_links = Functional.films_pages(links, URL)
    #Из ссылок с фильмами отбираются id
    print('Началась выборка id фильмов')
    id_list = Functional.id_separator(film_links)
    print(id_list)
    #Проверяем, если данные ссылки отсутвуют итоговом и соответствуют требованиям, то сохраняем в итоговый
    print('Началось включение id фильмов в результирующий список')
    Functional.result_list(DIR, id_list)
    print(f" Результирующий список включает в себя {len(set(open(DIR + '/result_list.txt').readlines()))} id")



"""
films_info = Media_parser(films_pages, headers)
with open(DIR + 'films.txt', 'w', encoding='utf-8') as info:
    for line in films_info:
        info.write(line)
"""