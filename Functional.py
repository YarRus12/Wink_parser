import requests
import re
import os

def films_pages(links: list, url: str) -> list:
    """Функция принимает в себя рабочие ссылки сайта и возвращает список  страницы с фильмами
    или с другим медиаконтентом"""
    list_of_films = []
    for line in links:
        patern = '(\/media_items\/media_items\/.*)'
        if re.search(patern, line) is not None:
            list_of_films.append(line)
    print(f'Отобрано {len(list_of_films)} ссылок с медиа контентом')
    return list_of_films

def id_separator(content: list) -> list:
    """Функция принимет в список ссылок на медиафайлы.
    И возвращает файл с id медиафайлов. "Этот предварительный этап можно было бы опустить,
    но он является удобным страхующим механизмом от потери данных"""
    number = 0
    id_list = []
    for line in content:
        *args, id = line.split('/')
        if id.isdigit():
            id_list.append(id)
            number += 1
    print(f'{number} id отобраны для включения в итоговый файл')
    return id_list


def result_list(DIR: str, id_list: list):
    """Функция принимает в себя путь и список id медиа файлов
    Сверяет новые id медиа файлов со старыми и дописывает их в результирующий список"""
    with open(DIR + '/result_list.txt', 'a', encoding='utf-8') as result:
        all_id = open(DIR + '/result_list.txt').readlines()
        all_id = [id.rstrip() for id in all_id]
        new = []
        for new_id in id_list:
            print(new_id)
            if new_id.rstrip() not in all_id:
                new.append(new_id+'\n')
        for id in new:
            result.write(id)
        print(f'В файл {DIR+"/result_list.txt"} дописаны {len(new)} id')


def working_check(links: list, headers: str) -> list:
    """Функция принимает в себя список ссылок и заголовки,
    проверяет работоспособность ссылок и возвращает список работоспособных ссылок"""
    working_links = []
    n = 0
    for link in links:
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            working_links.append(link)
            n += 1
        #    print(f'Обнаруженная ссылка № {n} {link} работает и добавлена в список')
        #else:
        #    print(f'Обнаруженная ссылка № {n} {link} не отвечает')
    print(f'Работоспособны {n} ссылок')
    return working_links

if __name__ == '__main__':
    list_of_films = films_pages()
    id_separator()
    working_check()