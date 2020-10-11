from random import randint
n = int(input("请输入一个自然数n"))
x = list()
while(len(x) != n):
    a = randint(1,5*n)
    if a not in x:
        x.append(a)
print(x)
for i in x[::-1]:
    if i%2==1:
        x.remove(i)
print(x)