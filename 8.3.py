import re
x = input()
# y = re.findall('[ \.\,][a-zA-Z]([a-zA-Z]+)[a-zA-Z]',x)
y = re.search('[a-zA-Z][A-Z][a-zA-Z]',x)
str = x[y.span()[0]+1].lower()
y = x[0:y.span()[0]+1]+ str + x[y.span()[1]:]
print(y)