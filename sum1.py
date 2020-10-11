from functools import reduce
x = int(input("请输入x"))
n = int(input("请输入n"))
a = list()
a = [0]*(n+1)
a[1]=x
for i in range(1,n):
    a[i+1]=a[i]+x*10**i
sum = 0
#for i in range(1,n+1):
#    sum+=a[i]
sum = reduce(lambda b,c:b+c,a)
print("sum = %d" % sum)