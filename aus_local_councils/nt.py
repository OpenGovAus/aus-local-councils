from bs4 import BeautifulSoup
from requests import get

url = 'https://www.lgant.asn.au/councils-2/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'} # 2000 IQ security bypass

def get_councils():
    _councils = []
    council_names = BeautifulSoup(get(url, headers=headers).text, 'lxml').find_all('h5', {'class': 'et_pb_toggle_title'})
    for council in council_names[1:]:
        _councils.append(council.text.strip().title())
    return(_councils)

councils = get_councils()