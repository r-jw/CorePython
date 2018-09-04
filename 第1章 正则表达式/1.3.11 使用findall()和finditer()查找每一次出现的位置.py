import re

s = 'This and that.'
m = re.findall(r'(th\w+) and (th\w+)', s, re.I)
print(m)

m1 = re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next__().group()
print(m1)

m2 = re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next__().group(1)
print(m2)

m3 = re.finditer(r'(th\w+) and (th\w+)', s, re.I).__next__().group(2)
print(m3)

m4 = [g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)]
print(m4)

m5 = re.findall(r'(th\w+)', s, re.I)
print(m5)

print('*' * 20)

it = re.finditer(r'(th\w+)', s, re.I)
g = it.__next__()
print(g.groups())
print(g.group(1))
print(g.group())

g = it.__next__()
print(g.groups())
print(g.group(1))

m6 = [g.group(1) for g in re.finditer(r'(th\w+)', s, re.I)]
print(m6)



