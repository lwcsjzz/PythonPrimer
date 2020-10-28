def chu(s):
    a = []
    for i in s:
        if i in a:
            a.remove(i)
            a.append(i)
        else:
            a.append(i)
    return(a)
s = input()
print(chu(s))