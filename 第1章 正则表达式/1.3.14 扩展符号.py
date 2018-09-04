import re

m = re.findall(r'http://(?:\w+\.)*(\w+\.com)', 'http://google.com http://www.google.com http://code.google.com')
print(m)

m = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212').groupdict()
print(m)

m = re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '\g<areacode> \g<prefix>-xxxx', '(800) 555-1212')
print(m)