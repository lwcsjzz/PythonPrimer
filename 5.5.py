def cycle (list):
    a = []
    for i in list:
        yield i
        a.append(i)
    while True :
        for i in list:
            yield i
for i in cycle('abc'):
    print(i)