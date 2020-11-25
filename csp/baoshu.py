def fun():
    n, k = map(int, input().split())
    a = [0] * n
    b = n
    num = 1
    while 1:
        for j in range(n):
            if ((num % k == 0 or num % 10 == k) and a[j] == 0):
                a[j] = 1
                b -= 1
                num += 1
            if a[j] == 0:
                num += 1
            if b == 1:
                for i in range(n):
                    if a[i] == 0:
                        print(i + 1)
                return


fun()