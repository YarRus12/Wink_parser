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

def id_separator(content: list) -> (list,str):
    """Функция принимет в список ссылок на медиафайлы.
    И возвращает список id медиафайлов и часть адреса общего для медиафайлов. "Этот предварительный этап можно было бы опустить,
    но он является удобным страхующим механизмом от потери данных"""
    id_list = []
    films_link = ''
    for line in content:
        *args, id = line.split('/')
        if id.isdigit():
            id_list.append(id)
            #films_links.append(line)
    films_link = content[0].split('/'+str(id))
    print(f'{len(id_list)} id отобраны для включения в итоговый файл')
    return films_link, id_list


def result_list(DIR: str, id_list: list, films_link: str):
    """Функция принимает в себя путь и список id медиа файлов и часть ссылки на медиматериалы
    Сверяет новые id медиа файлов со старыми и дописывает их в результирующий список, вмсете с ссылками на них"""
    with open(DIR + '/result_list.txt', 'a', encoding='utf-8') as result:
        all_id = open(DIR + '/result_list.txt').readlines()
        all_id = [line.rstrip() for line[0] in all_id]
        new = []
        for new_id in id_list:
            #print(new_id)
            """Это можно сделать лучше"""
            if new_id.rstrip() not in all_id:
                new.extend((new_id+','), films_link+id+'\n')
        for id in new:
            result.write(id)
            """
            Немного изменил логику работы кода, функция separator теперь возвращает ссылку на 
            фильм без id и список id. А функция добавления в итоговый файл созвращает текстовый 
            """

    print(f'В файл {DIR+"/result_list.txt"} дописаны {len(new)} id')


def working_check(links: list, headers: str) -> list:
    """Функция принимает в себя список ссылок и заголовки,
    проверяет работоспособность ссылок и возвращает список работоспособных ссылок"""
    working_links = []
    for link in links:
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            working_links.append(link)
        #    print(f'Обнаруженная ссылка № {n} {link} работает и добавлена в список')
        #else:
        #    print(f'Обнаруженная ссылка № {n} {link} не отвечает')
    print(f'Работоспособны {len(working_links)} ссылок')
    return working_links

if __name__ == '__main__':
    list_of_films = films_pages()
    id_separator()
    working_check()


