import requests
from urllib.request import urlopen
from urllib.response import addinfourl
import urllib
from bs4 import BeautifulSoup
import re
from fake_user_agent.main import user_agent
import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

def dinamic_page_open(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        """Применение опции открытия браузера в фоновом режиме"""
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        """Открытие страницы вживую"""
        #driver = webdriver.Chrome()#Открытие страницы вживую
        #driver.get(url) #Открытие страницы вживую
        SCROLL_PAUSE_TIME = 5
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        iterations = 0
        while iterations < 30:
        #while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            iterations += 1
            print(f'Программа успешно прокрутила страницу вниз {iterations} раз(-а)')
        time.sleep(SCROLL_PAUSE_TIME)
        html_content = driver.page_source
        #driver.close()
        return html_content

def parse_pages(url, headers):
        Links = []
        html_content = dinamic_page_open(url, headers)
        soup = BeautifulSoup(html_content, 'html.parser')
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
        print(f"Обнаружено {len(Links)} ссылок")
        return Links

def working_check(links, headers):
    #Проверяем что ссылки рабочие
    working_links = []
    n = 1
    for link in links:
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            working_links.append(link)
            print(f'Обнаруженная ссылка № {n} {link} работает и добавлена в список')
        else:
            print(f'Обнаруженная ссылка № {n} {link} не отвечает')
        n += 1
    return working_links

if __name__ == '__main__':
    links = parse_pages()
    working_check()

#for x in working_links: print(x)