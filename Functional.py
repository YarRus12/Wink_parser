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


def write_content(DIR, name, content):
    with open(DIR + name, 'w', encoding='utf-8') as info:
        number = 1
        for line in content:
            info.write(line+'\n')
            print(f'{number} {line} записана в файл{name}')
            number += 1

if __name__ == '__main__':
    list_of_films = films_pages()
    write_content()