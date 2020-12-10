from sys import int_info
from requests import get
from bs4 import BeautifulSoup

url = 'https://www.olg.nsw.gov.au/public/local-government-directory/'

def get_councils():
    council_list = []
    _councils_html = BeautifulSoup(get(url).text, 'lxml').find('ul', {'class': 'accordion accordion-child'}).find_all('li')
    for i in _councils_html:
        council_list.append(i.find('a').text)
    return(council_list)

councils = get_councils()