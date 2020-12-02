r, y, g = map(int, input().split())
n = int(input())
time = 0
for i in range(n):
    k, t = map(int, input().split())
    if k == 0 or k == 1:
        time += t
    elif k == 2:
        time = time +r +t
print(time)