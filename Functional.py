import re
import os

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
    number = 0
    with open(DIR + name, 'w', encoding='utf-8') as info:
        for line in content:
            *args, id = line.split('/')
            print(id)
            if id.isdigit():
                info.write(id+'\n')
                number += 1
            #print(f'Ссылка {number} {line} записана в файл{name}')
    print(f'{number} ссылок записаны в файл {name}')


def result_list(DIR: str, path: str):
    with open(DIR + '/result_list.txt', 'a', encoding='utf-8') as result:
        with open(path, 'r', encoding='utf-8') as pool:
            all_id = open(DIR + '/result_list.txt').readlines()
            all_id = [id.rstrip() for id in all_id]
            print(all_id)
            new = []
            for new_id in pool:
                if new_id.rstrip() not in all_id:
                    new.append(new_id)
            print(new)
            for id in new:
                result.write(id)


#DIR = os.path.dirname(os.path.abspath(__file__))
#result_list(DIR, DIR+'\pool.txt')


if __name__ == '__main__':
    list_of_films = films_pages()
    write_content()