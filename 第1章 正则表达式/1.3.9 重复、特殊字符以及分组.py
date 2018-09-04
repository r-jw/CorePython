import re

patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@xxx.com')
if m is not None:
    print(m.group())

m = re.match(patt, 'nobody@www.xxx.com')
if m is not None:
    print(m.group())

patt1 = '\w+@(\w+\.)*\w+\.com'
m = re.match(patt1, 'nobody@www.xxx.yyy.zzz.com')
if m is not None:
    print(m.group())

m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None:
    print(m.group())

m = re.match('\w\w\w-\d\d\d', 'abc-xyz')
if m is not None:
    print(m.group())

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())

m = re.match('(a(b))', 'ab')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
