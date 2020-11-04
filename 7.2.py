def fun(s):
    a = s.split(" ")
    b = []
    for i in a[::-1]:
        b.append(i)
    return b
s = input()
print(fun(s))