from requests import get
from bs4 import BeautifulSoup

url = 'https://www.nqlegal.com.au/townsville-conveyancing-solicitors/queensland-councils-shires/' # Using this because the official government directory returns a 404 (very professional)

def get_councils():
    _councils = []
    rows = BeautifulSoup(get(url).text, 'lxml').find_all('table')[-1].find_all('tr')
    for row in rows[1:]:
        _councils.append(row.find('td').text)
    return(_councils)

councils = get_councils()