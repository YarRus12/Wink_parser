import re
# Функция отбора из рабочих ссылков сайта тех, где содержатся страницы с фильмами
def films_pages(url: str, path: str) -> list:
    list_of_films = []
    with open(path, 'r', encoding='utf-8') as info:
        for line in info:
            #re.compile(r'')
            for link in line.find_all('a', href=re.compile('(\/media_items\/.*)')):
                if link.attrs['href'] is not None:
                    if link.attrs['href'] not in list_of_films:
                        if link.attrs['href'].startswith('/'):
                            list_of_films.append(url + link.attrs['href'])
                        else:
                            list_of_films.append(link.attrs['href'])
            else:
                print("Connection Error")
            return list_of_films