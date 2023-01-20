import requests
from bs4 import BeautifulSoup
from time import sleep 
 
headers = {
        "User-Agent": 
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

def get_url():
    for page in range(1, 10000):
        try:
            url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'
            requests_data = requests.get(url, headers = headers)

            soup = BeautifulSoup(requests_data.text, 'lxml')

            array_data = soup.find_all("div", class_ = "col-lg-4 col-md-6 mb-4")

            for data in array_data:
                link_page = "https://scrapingclub.com" + data.find('a').get('href')
                yield link_page
        except:
            yield False

def get_data_array():
    for page_url in get_url():
        if not get_url:
            break
        #ПС: писать код таким образом - ХАРАМ.
        requests_data = requests.get(page_url, headers = headers)

        sleep(3)

        soup = BeautifulSoup(requests_data.text, 'lxml')
        data_page = soup.find("div", class_ = "card mt-4 my-4")
    
        link_img = "https://scrapingclub.com" + data_page.find('img', class_='card-img-top img-fluid').get('src')
        name_ctl = data_page.find('h3', class_='card-title').text.replace("\n", "")
        price_ctl = data_page.find('h4').text
        text_ctl = data_page.find('p', class_="card-text").text
    
        download(link_img)
        yield name_ctl, price_ctl, text_ctl, link_img

def download(url):
    resp = requests.get(url, stream = True)
    r = open("images_result\\" + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024): 
        r.write(value)
    r.close()