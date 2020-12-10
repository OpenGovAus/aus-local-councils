import json
from requests import get

url = 'https://lgdirectory.dlgrma.qld.gov.au/php/councilList.php'

def get_councils():
    _councils = []
    council_data = json.loads(get(url).text)
    for council in council_data:
        _councils.append(council['councilname'])
    return(_councils)

councils = get_councils()