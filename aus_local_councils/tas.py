from requests import get
from bs4 import BeautifulSoup

url = 'http://www.dpac.tas.gov.au/divisions/local_government/local_government_directory'

def get_councils():
    _councils = []
    council_names = BeautifulSoup(get(url).text, 'lxml').find('select', {'name': 'lgc'}).find_all('option')
    for council in council_names:
        _councils.append('%s Council' % (council.text))
    return(_councils)

councils = get_councils()