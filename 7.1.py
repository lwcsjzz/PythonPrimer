def number(s):
    a = 0
    c =[]
    b =[]
    for i in s:
        if i.isdigit() :
            c.append(i)
            if len(c) > a:
                b = c
                a = len(c)
        else:
            c = []
            d = ''.join(b)
    return d
s = input()
print(number(s))