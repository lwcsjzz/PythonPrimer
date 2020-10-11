n = int(input('请输入分数(0 - 100)'))
if n<60:
    print("不及格")
elif n>=60 and n<70:
    print("差")
elif n>=70 and n<80:
    print("中")
elif n>=80 and n<90:
    print("良")
else:
    print("优")