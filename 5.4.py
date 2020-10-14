def hv(list):
    for i in range(len(list)):
        a = 0
        if list[i]!=list[len(list)-i-1]:
            a+=1
    return a
list=input()
if hv(list):
    print("不是回文")
else:
    print("是回文")