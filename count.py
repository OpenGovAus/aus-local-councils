# This is an example script which will generate aus_councils.json, and will also tell you how many councils the package scrapes.

print('Getting local councils...')

import aus_local_councils.qld
print('1/7 qld.py')
import aus_local_councils.nsw
print('2/7 nsw.py')
import aus_local_councils.nt
print('3/7 nt.py')
import aus_local_councils.sa
print('4/7 sa.py')
import aus_local_councils.tas
print('5/7 tas.py')
import aus_local_councils.vic
print('6/7 vic.py')
import aus_local_councils.wa
print('7/7 wa.py')
import json

nsw_councils = aus_local_councils.nsw.councils
nt_councils = aus_local_councils.nt.councils
qld_councils = aus_local_councils.qld.councils
sa_councils = aus_local_councils.sa.councils
tas_councils = aus_local_councils.tas.councils
vic_councils = aus_local_councils.vic.councils
wa_councils = aus_local_councils.wa.councils

print('Calculating all_councils...')

all_councils = sa_councils + nt_councils + nsw_councils + tas_councils + vic_councils + wa_councils + qld_councils

print('%d local councils were found.' % (len(all_councils)))
print('Writing to aus_councils.json...')

with open('aus_councils.json', 'w') as file:
    json_data = json.dumps({'QLD': qld_councils,
    'NSW': nsw_councils,
    'NT': nt_councils,
    'SA': sa_councils,
    'TAS': tas_councils,
    'VIC': vic_councils,
    'WA': wa_councils}, indent=2)
    file.write(json_data)
    print('Done.')