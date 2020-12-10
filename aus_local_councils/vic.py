from requests import get
from bs4 import BeautifulSoup

url = 'https://www.viccouncils.asn.au/find-your-council/council-contacts-list'

def get_councils():
    _council_names = []
    rows = BeautifulSoup(get(url).text, 'lxml').find('table', {'id': 'table19340'}).find_all('tr')
    for row in rows:
        _council_names.append(row.find('p').text)
    return(_council_names)

councils = get_councils()