import re
# Функция отбора из рабочих ссылков сайта тех, где содержатся страницы с фильмами

def films_pages(path):
    list_of_films = []
    with open(path, 'r', encoding='utf-8') as info:
        for line in info:
            #re.compile(r'')
            for link in line.find_all('a', href=re.compile('(\/media_items\/.*)')):
                list_of_films.append(link)
                # Не дописал смысл в том, что при совпадении строки с патерном строка сохраняется в множество set(),
                # Эти множества будут перебиратьс в дайльнейшим для распарсевания страниц и поиска элементов
