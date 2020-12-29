n,x,y=map(int,input().split())
address=[]
for i in range(n):
    a,b=map(int,input().split())
    distance=(x-a)**2+(y-b)**2
    address.append((distance,i+1))
address.sort()
for i in range(3):
    print(address[i][1])