import re

m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None:
    print(m.group())

m = re.match('[cr][23][dp][o2]', 'c2po')
if m is not None:
    print(m.group())

m = re.match('r2d2|c3po', 'c2do')
if m is not None:
    print(m.group())

m = re.match('r2d2|c3po', 'r2d2')
if m is not None:
    print(m.group())