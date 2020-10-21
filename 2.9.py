a,b,c=input().split( )
a=int(a)
b=int(b)
c=int(c)
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print("%d->%d->%d"%(a,b,c))