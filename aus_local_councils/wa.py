from requests import get
from bs4 import BeautifulSoup

url = 'https://walga.asn.au/About-Local-Government/Online-Local-Government-Directory?letter=&page='

def get_councils():
    _council_list = []
    for i in range(1,15):
        soup = BeautifulSoup(get(url + str(i)).text, 'lxml').find('div', {'class': 'col-md-12 main-content'}).find_all('div', {'class': 'data-council'})
        for council in soup:
            _council_list.append(council.find('a').text)
    return(_council_list)

councils = get_councils()