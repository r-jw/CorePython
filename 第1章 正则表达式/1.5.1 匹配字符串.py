import re

data = 'Wed Mar 20 12:08:14 2086::eumf@ynxn.net::3667435694-4-4'

patt = '^(Mon|Tue|Wed|Thu|Fri|Sta|Sun)'
m = re.match(patt, data)
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())

patt = '^(\w{3})'
m = re.match(patt, data)
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())

