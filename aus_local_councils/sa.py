from requests import get
from bs4 import BeautifulSoup

url = 'https://www.ecsa.sa.gov.au/council-links'

def get_councils():
    council_list = []
    _list = BeautifulSoup(get(url).text, 'lxml').find('div', {'class': 'content-text'}).find_all('li')
    for council in _list:
        council_list.append(council.text.replace('\u00a0', ' '))
    return(council_list)

councils = get_councils()