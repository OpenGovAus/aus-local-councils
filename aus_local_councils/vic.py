from requests import get
from bs4 import BeautifulSoup

url = 'https://knowyourcouncil.vic.gov.au/councils'

def get_councils():
    _council_names = []
    div = BeautifulSoup(get(url).text, 'lxml')
    councils = div.find_all('li')
    for council in councils[9:]:
        _council_names.append(council.text)
    return _council_names

councils = get_councils()