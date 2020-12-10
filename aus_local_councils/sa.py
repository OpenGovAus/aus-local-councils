from requests import get
from bs4 import BeautifulSoup

url = 'https://www.lga.sa.gov.au/sa-councils/councils-listing'

def get_councils():
    council_list = []
    _list = BeautifulSoup(get(url).text, 'lxml').find('div', id='content_container_538648')
    for entry in _list.find_all('li', {'class': 'sacouncils-listing-item'}):
        council_list.append(entry.text.strip())
    return council_list

councils = get_councils()