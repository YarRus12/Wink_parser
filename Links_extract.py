import requests
from urllib.request import urlopen
from urllib.response import addinfourl
import urllib
from bs4 import BeautifulSoup
import re
from fake_user_agent.main import user_agent

#В качестве URL передаем ссылку на сайт онлайн кинотеатра Wink
URL = 'https://wink.ru'
#Настраеваем липовый юзерагент для работы с защищенными сайтами
user_agent = user_agent("chrome")
#Передаем в переменную headers значения юзерагента
headers = {'accept': '*/*', 'user-agent': user_agent}

def without_post(url, headers):
    response = requests.get(url, headers=headers)
    Links = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        #регулярным выражением ищем все ссылки в html и собираем их по сайту
        for link in soup.find_all('a', href=re.compile('^(/|.*' + url + ')')):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in Links:
                    if link.attrs['href'].startswith('/'):
                        Links.append(url + link.attrs['href'])
                    else:
                        Links.append(link.attrs['href'])
    else:
        print("Connection Error")
    return Links

links = without_post(URL, headers)
working_links = []
#Проверяем что ссылки рабочие
for link in links:
    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        working_links.append(link)
        print(f'Ссылка {link} работает и добавлена в словарь добавлена')
    else:
        print(f'Ссылка {link} не отвечает')

for x in working_links: print(x)