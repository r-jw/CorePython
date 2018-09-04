import re

m = re.sub('X', 'Mr.Smith', 'attn:X\n\nDear X,\n')
print(m)

m = re.subn('X', 'Mr.Smith', 'attn:X\n\nDear X,\n')
print(m)

m = re .sub('[ae]', 'X', 'abcdef')
print(m)

print(re.subn('[ae]', 'X', 'abcdef'))

#将美式的日期表示法MM/DD/YY{,YY}格式转换为其他国家常用的格式DD/MM/YY{,YY}
patt = r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})'
m = re.sub(patt, r'\2/\1/\3', '2/20/91')
print(m)

m = re.sub(patt, r'\2/\1/\3', '2/20/1991')
print(m)
