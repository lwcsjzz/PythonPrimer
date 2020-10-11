head = int(input('请输入总的头数'))
jiao = int(input('请输入总的脚数'))
if 2*head<jiao and jiao<4*head and jiao%2==0:
    ji = 2*head-jiao//2
    tu = head - ji
else:
    print("输入错误")
print("鸡的个数为 %d" % ji)
print("兔子的个数为  %d" % tu)