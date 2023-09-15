from bs4 import BeautifulSoup
import requests

url = 'https://kinogo-official.ru/filmy/filmy-2021/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

film_names = soup.find_all('a', class_='kino-h')
film_info = soup.find_all('div', class_='k-label')

for name_item in film_names:
    print(name_item.text)
