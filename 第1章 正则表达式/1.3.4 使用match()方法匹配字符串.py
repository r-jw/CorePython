import re

m = re.match('foo', 'foo')  #模式匹配字符串
if m is not None:
    print(m.group())
    print(m)

m = re.match('foo', 'bar')
if m is not None: print(m.group())  #单行版本的if语句

m = re.match('foo', 'food on the table')
print(m.group())

print(re.match('foo', 'food onthe table').group())

