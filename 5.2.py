def ab(a,b):
    if a<b:
        a, b = b, a
    while b!=0:
        c=a%b
        a = b
        b = c
    return a
a=int(input())
b=int(input())
print(ab(a,b))