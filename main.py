import os
from input_modul import data_entry
from actions_modul import get_items

def start_parsing(start_page_, finishing_page_, link_page_, timer_, path_file_, download_path_):
    """
    Функция иницализирет все функии кода, тем самым начиная процесс работы
    Аргументы: 
              start_page_(int) - принимаем от пользовотеля начальную страницу в виде целого числа
              для парсинга 
              finishing_page_(int) - принимаем от пользовотеля кончечную страницу в виде целого числа
              для парсинга
              link_page_(string) - ссылка на сайт
              timer_(int) - принимем аргумент на указание сколько секунд надо задержовать в time.sleep(arg)
              path_file_(string) - принимаем место для сохранение Exsеl файла
              download_path_(string) - принимаем место для сохранение скачанных файлов
    Возвращает:
               null
    """
    items = list(get_items(start_page_, finishing_page_, link_page_, timer_, path_file_, download_path_))
    data_entry(path_file_, items)
    
    print("Процесс закончен!\nГотовые данные можете посмотреть в: {}".format(path_file_))


print("Добро пожаловать в TriplP! \n"
      "Софт предназначенный для парсинга. \n"
      "Для начало работы надо: \n"
      "1.Передать ссылку сайта для парсинга(в начем случае - https://scrapingclub.com/exercise/list_basic/page=1) \n"
      "2.Указать от какой страницы начать и заканчивать.(в диапазоне 1-7) \n"
      "3.Указать путь для сохранение данных. \n"
      "4.Потом просто ждать."
      )

link_page = input("\nПередайте ссылку на сайта: ")
start_page = input("\nУкажите начальную страницу: ")
finishing_page = input("\nУкажите заканчивающую страницу: ")
timer = input("\nУкажите сколько времени надо задерживать парсинг(таймер): ")
path_file = input("\nВнимания!!!Имя файла не должен повторятся со существуещими!?\nУкажите путь для сохранение Exsel данных: ")
download_path = input("\nУкажите путь для сохранение скачанных данных: ")

start_parsing(start_page, finishing_page, link_page, timer, path_file, download_path)