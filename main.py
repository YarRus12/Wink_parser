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

def write_content(DIR, name, content):
    with open(DIR + name, 'w', encoding='utf-8') as info:
        for line in content:
            info.write(line)
            print(f'{line} записана в файл')


#Поиск всех ссылок
links = Links_extract.without_post(URL, headers)
#Проверка работоспособности ссылок
working_links = Links_extract.working_check(links, headers)
print(working_links)

#Все работоспособные ссылки сохраняем в отдельный файл

write_content(DIR, '\link.txt', working_links)

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