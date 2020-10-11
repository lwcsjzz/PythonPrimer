from random import randint
x = list()
for i in range(20):
    a = randint(-100,100)
    x.append(a)
a = sorted(x[0:10])
b = sorted(x[10:20],reverse=True)
print(a)
print(b)