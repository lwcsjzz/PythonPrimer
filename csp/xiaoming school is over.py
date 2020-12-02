light=[0,0,0]
light[0], light[2], light[1] = map(int, input().split())
n = int(input())
time = 0
for i in range(n):
    k, t = map(int, input().split())
    if k == 0:
        time+=t
    else:
        sum = light[1]+light[0]+light[2]
        if k == 1:
            k = 0
        elif k == 3:
            k =1
        t = (light[k] - t +time)%sum
        while(t>light[k]):
            t -= light[k]
            k =(k+1)%3
        if k == 0:
            time +=light[k]-t
        elif k==2:
            time += light[k]-t+light[0]
print(time)