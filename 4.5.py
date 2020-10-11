import random
dic = {0:0,1:0,2:0,3:0,4:0}
a=random.randint(0,4)
dic[a]=1
while(dic[int(input("请输入狐狸的位置"))]!=1):
    print("很遗憾没有抓到")
    n = random.randint(0,1)
    if a==0:
        dic[0]=0
        dic[1]=1
        a=1
    elif a==4:
        dic[4]=0
        dic[3]=1
        a=3
    else:
        if n==0:
            dic[a-1]=1
            dic[a]=0
            a-+1
        else:
            dic[a+1]=1
            dic[a]=0
            a+=1
print("恭喜你抓到了")