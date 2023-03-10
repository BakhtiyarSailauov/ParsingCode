import requests
from bs4 import BeautifulSoup
from time import sleep 
 
headers = {
        "User-Agent": 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

"""
get_page - предназна для того что-бы вернуть все данные из одного страницы

Изначально, с помошью request мы вернем весь HTML-код из одного страницы
Потом, через BeautifulSoup, отредактируем код красиво, для дальнейшего работы
От одного страницы другому переходим с помощью цикла for

Из-за особенности страницы, мы будем сортировать все данные с помошью блока <div>.

Сама функция реализована как генератор, и каждый раз будет вернуть один блок из всего листа.
"""
def get_page(start_page, finishing_page, link):
    """
    Функция-генератор возвращает ссылку на конкретную страницу с каталогом для парсинга, 
    сортируя его с помощью BeautylSoup и requests

    Аргументы: 
              start_page(int) - принимаем от пользовотеля начальную страницу в виде целого числа
              для парсинга 
              finishing_page(int) - принимаем от пользовотеля кончечную страницу в виде целого числа
              для парсинга
              link(string) - ссылка на сайт
    Возвращает:
               link_pahe(string) -  ссылка каталого из сайта
    """
    for page in range(int(start_page), int(finishing_page)):
        print((100*'\n') + "Подождите! Идет процесс парсинга. Мы на {} странице. ".format(page))
        url_array = link.split("/")
        url_array.append(f'?page={page}')
        url = "/".join(url_array)
        requests_data = requests.get(url, headers = headers)

        soup = BeautifulSoup(requests_data.text, 'lxml')

        array_data = soup.find_all("div", class_ = "col-lg-4 col-md-6 mb-4")

        for data in array_data:
            link_page = "https://scrapingclub.com" + data.find('a').get('href')
            yield link_page


def get_items(start_page, finishing_page, link, timer, file_path, download_path):
    """
    Функция-генератор возвращает конкретную список аргументов для парсинга, 
    сортируя его с помощью BeautylSoup и requests

    Аргументы: 
              start_page(int) - принимаем от пользовотеля начальную страницу в виде целого числа
              для парсинга 
              finishing_page(int) - принимаем от пользовотеля кончечную страницу в виде целого числа
              для парсинга
              link(string) - ссылка на сайт
              timer(int) - принимем аргумент на указание сколько секунд надо задержовать в time.sleep(arg)
              file_path(string) - принимаем место для сохранение Exsеl файла
              download(string) - принимаем место для сохранение скачанных файлов
    Возвращает:
               аргумент данных из парсинга(name_ctl, price_ctl, text_ctl, link_img)
    """
    for page_url in get_page(start_page, finishing_page, link):
        #ПС: писать код таким образом - ХАРАМ.
        requests_data = requests.get(page_url, headers = headers)

        sleep(int(timer))

        soup = BeautifulSoup(requests_data.text, 'lxml')
        data_page = soup.find("div", class_ = "card mt-4 my-4")
    
        link_img = "https://scrapingclub.com" + data_page.find('img', class_='card-img-top img-fluid').get('src')
        name_ctl = data_page.find('h3', class_='card-title').text.replace("\n", "")
        price_ctl = data_page.find('h4').text
        text_ctl = data_page.find('p', class_="card-text").text
    
        download(link_img, download_path)
        yield name_ctl, price_ctl, text_ctl, link_img

def download(url, download_path):
    """
    Функция cкачивает изображение(в целом любого типа файла), с помощью requests.get(stream=True) 

    Аргументы: 
              url(string) - ссылка сайта
              download(string) - принимаем место для сохранение скачанных файлов
    Возвращает:
               null
    """
    resp = requests.get(url, stream = True)
    r = open("{}\\".format(download_path) + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024): 
        r.write(value)
    r.close()