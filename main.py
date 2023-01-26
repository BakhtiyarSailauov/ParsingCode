import os
from input_modul import data_entry
from actions_modul import get_items

def start_parsing(start_page_, finishing_page_, link_page_, timer_, path_file_, download_path_):
    items = list(get_items(start_page_, finishing_page_, link_page_, timer_, path_file_, download_path_))
    data_entry(path_file_, items)


print("Добро пожаловать в TriplP! \n"
      "Софт предназначенный для парсинга. \n"
      "Для начало работы надо: \n"
      "1.Передать ссылку сайта для парсинга(в начем случае - https://scrapingclub.com/exercise/list_basic/page=1) \n"
      "2.Указать от какой страницы начать и заканчивать.(в диапазоне 1-7) \n"
      "3.Указать путь для сохранение данных. \n"
      "4.Потом просто ждать."
      )

link_page = input("Передайте ссылку на сайта: ")
start_page = input("Укажите начальную страницу: ")
finishing_page = input("Укажите заканчивающую страницу: ")
timer = input("Укажите сколько времени надо задерживать парсинг(таймер): ")
path_file = input("Укажите путь для сохранение Exsel данных: ")
download_path = input("Укажите путь для сохранение скачанных данных: ")

start_parsing(start_page, finishing_page, link_page, timer, path_file, download_path)