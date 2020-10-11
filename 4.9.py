n = 0
global b
b = 0
def xiaoming(a,n):
    n+=a
    global b
    if n==15:
        b+=1
    elif n>15:
        b+=0
    else:
        xiaoming(1,n)
        xiaoming(3,n)
xiaoming(1, n)
xiaoming(3, n)
print(b)