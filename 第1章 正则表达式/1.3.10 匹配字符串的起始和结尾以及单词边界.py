import re

m = re.search('^The', 'The end.')
if m is not None:
    print(m.group())

m = re.search('^The', 'end. The')
if m is not None:
    print(m.group())

m = re.search(r'\bthe', 'bite the dog')  #在边界
if m is not None:
    print(m.group())

m = re.search(r'\bthe', 'bitethe dog')  #有边界
if m is not None:
    print(m.group())

m = re.search(r'\Bthe', 'bitethe dog')  #没有边界
if m is not None:
    print(m.group())