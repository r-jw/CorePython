import re

anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None:
    print(m.group())

m = re.match(anyend, 'end')
if m is not None:
    print(m.group())

m = re.match(anyend, '\nend')
if m is not None:
    print(m.group())

m = re.search('.end', 'The end')    #在搜索中匹配' '
if m is not None:
    print(m.group())

patt314 = '3.14'    # 表示正则表达式的点号
pi_patt = '3\.14'   # 表示字面量的点号 （dec.point）
m = re.match(pi_patt, '3.14')   # 精确匹配
if m is not None:
    print(m.group())

m = re.match(patt314, '3014')   # 点号匹配0
if m is not None:
    print(m.group())

m = re.match(patt314, '3.14')   # 点号匹配 '.'
if m is not None:
    print(m.group())

