import os
import requests
from urllib.request import urlopen
from urllib.response import addinfourl
import urllib
from bs4 import BeautifulSoup
import re
from fake_user_agent.main import user_agent
import Links_extract

DIR = os.path.dirname(os.path.abspath(__file__))
#В качестве URL передаем ссылку на сайт онлайн кинотеатра Wink
URL = 'https://wink.ru/media_items'
#Настраеваем липовый юзерагент для работы с защищенными сайтами
user_agent = user_agent("chrome")
#Передаем в переменную headers значения юзерагента
headers = {'accept': '*/*', 'user-agent': user_agent}

#Поиск всех ссылок
links = Links_extract.without_post(URL, headers)
#Проверка работоспособности ссылок
working_links = Links_extract.working_check(links)

#Все работоспособные ссылки сохраняем в отдельный файл
with open(DIR + 'links.txt', 'w', encoding='utf-8') as info:
    for line in working_links:
        info.write(line)


