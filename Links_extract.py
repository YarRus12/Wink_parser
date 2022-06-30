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
from selenium import webdriver

import os


def dinamic_page_open(url: str, headers: str):
    """Функция принимает в себя адрес и заголовки, обращается к вэб странице, прокручивает страницу вниз,
    извлекает контент в html файл"""
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        """Применение опции открытия браузера в фоновом режиме"""
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)

        """Открытие страницы в режиме реального времени"""
        #driver = webdriver.Chrome()#Открытие страницы вживую
        #driver.get(url) #Открытие страницы вживую

        #Время на прокрутку страницы
        SCROLL_PAUSE_TIME = 3
        # Определение высоты страницы
        last_height = driver.execute_script("return document.body.scrollHeight")
        # Счетчик итераций
        iterations = 0
        # Цикл прокручивающий страницу вниз
        while iterations < 20:
        #while True:
            # Выполнение скрипта по прокрутке страницы в самый низ
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Ожидание прогрузки страницы
            time.sleep(SCROLL_PAUSE_TIME)
            # Переопределение высоты страницы, если высота не изменилась, то скрипт достиг дна страницы
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            iterations += 1
            print(f'Программа успешно прокрутила страницу вниз {iterations} раз(-а)')

        html_content = driver.page_source
        return html_content

def parse_pages(url: str, headers: str) -> list:
    """Функция принимает в себя адрес и заголовки
    на странице ссылки и возвращает список ссылок"""
    Links = []
    html_content = dinamic_page_open(url, headers)
    soup = BeautifulSoup(html_content, 'lxml')
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


if __name__ == '__main__':
    links = parse_pages()
    dinamic_page_open()