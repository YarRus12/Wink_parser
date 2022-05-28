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
        number = 1
        for line in content:
            info.write(line+'\n')
            print(f'{number} {line} записана в файл')
            number += 1


#Поиск всех ссылок
links = Links_extract.parse_pages(URL, headers)
#Проверка работоспособности ссылок
working_links = Links_extract.working_check(links, headers)
#Все работоспособные ссылки сохраняем в предварительный файл
write_content(DIR, '\pool.txt', working_links)




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