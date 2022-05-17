import requests
from urllib.request import urlopen
from urllib.response import addinfourl
import urllib
from bs4 import BeautifulSoup
import re
from fake_user_agent.main import user_agent

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

def working_check(links):
    #Проверяем что ссылки рабочие
    working_links = []
    for link in links:
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            working_links.append(link)
            print(f'Ссылка {link} работает и добавлена в словарь добавлена')
        else:
            print(f'Ссылка {link} не отвечает')
    return working_links

links = without_post(URL, headers)


#for x in working_links: print(x)