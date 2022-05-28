import requests
from urllib.request import urlopen
from urllib.response import addinfourl
import urllib
from bs4 import BeautifulSoup
import re
from fake_user_agent.main import user_agent

# В данном скрипте информация со списком страниц будет передаваться в Functional.films_pages
# И далее страницы с фильмами будут распарсеватсья на интересующие элементы, а именно



"""
def get_conteent(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-card')
    goods = []
    for item in items:
        good = item.find('span', class_='goods-name').get_text(strip=True)
        brand = (item.find('strong', class_='brand-name').get_text(strip=True))[:-1]
        low_price = str(item.find('ins', class_='lower-price'))
        low_price = "".join([s for s in re.findall(r'-?\d+\.?\d*', low_price)])
        full_price = str(item.find('span', class_='price-old-block'))
        full_price = "".join([s for s in re.findall(r'-?\d+\.?\d*', full_price)])
        id = item.find('div', class_='product-card__wrapper').find('a').get('href')
        id = "".join([s for s in re.findall(r'-?\d+\.?\d*', id)])
        href = item.find('div', class_='product-card__wrapper').find('a').get('href')

        goods.append(
            {
                'id' : id,
                'good': good,
                'brand': brand,
                'sales price': low_price,
                'full price': full_price,
                'link': HOST+href
            }
        )
    return goods
"""












class page_parser:
    def __init__(self, page, films_url, headers):
        response = requests.get(films_url+page, headers=headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
            self.id = page


class film_reaper(page_parser):
    def __init__(self):
        pass
    def reaper(self):
        # Вытаскиваем наименование фильма
        for link in self.soup.find('a', href= 'root_r1ru04lg name_ntuymo6 root_header1_r1swja1w', text=re.compile('media-item-name')):
            if link.attrs['root_r1ru04lg name_ntuymo6 root_header1_r1swja1w'] is not None:
                self.film_name = link.attrs['root_r1ru04lg name_ntuymo6 root_header1_r1swja1w']
                print(self.film_name)
"""
                            
                                    # Вытаскиваем дату релиза, продолжительность и возрастные ограничения фильма
                                    for link in soup.find_all('a', href=re.compile('^\/movies\?years=.*')):
                                        if link.attrs['href'] is not None:
                                            self.release_date = ((link.attrs['href']).split('=')[-1])
                                            # под этим же якорем
                                            self.duration = link.attrs['span']
                                            # под этим же якорем
                                            self.film_age_rating = link.attrs['span']
                            
                                    # Вытаскиваем средний рейтинг фильма по версии Wink
                                    # На самом деле вытаскиваем только 1 цифру среднего рейтинга
                                    for link in soup.find_all('???', '????'=re.compile('rating_wink_int_part_r17g8ivt')):
                                        if link.attrs['href'] is not None:
                                            self.avr_grade = (link.attrs['????'])
                                    # Вытаскиваем описание фильма
                                    for link in soup.find('??', ???=re.compile('media-item-description$')):
                                        if link.attrs['????'] is not None:
                                            self.description = link.attrs['????']
                                    # Вытаскиваем жанр фильма
                                    for link in soup.find('a', href=re.compile('^movies\?vod_genres')):
                                        if link.attrs['href'] is not None:
                                            self.genre = link.attrs['href'].split('=')[0]
                                    # Вытаскиваем имя режиссера
                                    for link in soup.find('??', href=re.compile('root_r1ru04lg name_ntjejvp bold_bgok4v root_subtitle1_r18emsye')):
                                        if link.attrs['????'] is not None:
                                                surname = link.attrs['????']
                                    for link in soup.find('????', href=re.compile('root_r1ru04lg name_ntjejvp root_subtitle2_rt60wi')):
                                        if link.attrs['????'] is not None:
                                            name = link.attrs['????']
                                    self.main_director = f'{surname} {name}'
                            
                                    return self.id, self.film_name, self.release_date, self.duration, self.film_age_rating, self.link, self.main_director
                            
 """