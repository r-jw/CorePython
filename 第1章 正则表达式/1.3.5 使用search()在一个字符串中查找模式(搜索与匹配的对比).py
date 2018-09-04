import re

m = re.match('foo', 'seafood')
if m is not None: print(m.group())

m = re.search('foo', 'seafood')
if m is not None: print(m.group())
