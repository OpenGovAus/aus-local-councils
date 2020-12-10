# This is an example script which will generate aus_councils.json, and will also tell you how many councils the package scrapes.

import aus_local_councils.qld
import aus_local_councils.nsw
import aus_local_councils.nt
import aus_local_councils.sa
import aus_local_councils.tas
import aus_local_councils.vic
import aus_local_councils.wa
import json

all_councils = aus_local_councils.sa.councils + aus_local_councils.nt.councils + aus_local_councils.nsw.councils + aus_local_councils.tas.councils + aus_local_councils.vic.councils + aus_local_councils.wa.councils + aus_local_councils.qld.councils

print('%d local councils were found.' % (len(all_councils)))

open('aus_councils.json', 'w').write(json.dumps({'QLD': aus_local_councils.qld.councils,
'NSW': aus_local_councils.nsw.councils,
'NT': aus_local_councils.nt.councils,
'SA': aus_local_councils.sa.councils,
'TAS': aus_local_councils.tas.councils,
'WA': aus_local_councils.wa.councils}, indent=2))