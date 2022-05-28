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

number_of_iter = 1
for i in range(number_of_iter):
    Functional.result_list(DIR, DIR + '\pool.txt')
    """#Поиск всех ссылок
    print('Началась процедура поиска всех ссылок на странице')
    links = Links_extract.parse_pages(URL, headers)
    #Проверка работоспособности ссылок
    print('Началась процедура проверки работоспособности ссылок')
    working_links = Links_extract.working_check(links, headers)
    #Все работоспособные ссылки сохраняем в предварительный файл
    print('Началась процедура записи id фильмов')
    Functional.write_content(DIR, '\pool.txt', working_links)"""
    #Проверяем, если данные ссылки отсутвуют итоговом и соответствуют требованиям, то сохраняем в итоговый





#
#
#Вызывается функция films_pages из блока Functional
#films_pages = Functional.films_pages(DIR + 'links.txt')

"""
films_info = Media_parser(films_pages, headers)
with open(DIR + 'films.txt', 'w', encoding='utf-8') as info:
    for line in films_info:
        info.write(line)
"""