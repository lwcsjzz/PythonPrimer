a = int(input())
n = 1
if a == 1:
    print("%.3f" % n)
elif a == 0:
    print("%.3f" % n)
else:
    for i in range(2, a + 1):
        j = 2 * i - 1
        if i % 2 == 0:
            n -= (i / j)
        else:
            n += (i / j)
print("{:.3f}".format(n))