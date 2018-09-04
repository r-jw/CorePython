import re

data = 'Wed Mar 20 12:08:14 2086::eumf@ynxn.net::3667435694-4-4'

patt = '\d+-\d+-\d+'
print(re.search(patt, data).group())

patt = '.+\d+-\d+-\d+'
print(re.search(patt, data).group())

patt = '.+(\d+-\d+-\d+)'
print(re.search(patt, data).group(1))

patt = '.+?(\d+-\d+-\d+)'
print(re.search(patt, data).group(1))

patt = '-(\d+)-'
print(re.search(patt, data).group(1))