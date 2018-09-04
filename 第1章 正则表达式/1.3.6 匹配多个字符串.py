import re

bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print(m.group())

m = re.match(bt, 'blt')
if m is not None:
    print(m.group())

m = re.match(bt, 'He bit me')
if m is not None:
    print(m.group())

m = re.search(bt, 'He bit me')
if m is not None:
    print(m.group())