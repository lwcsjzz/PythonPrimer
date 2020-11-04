from random import randint
import re
def tiao(n):
    a = 0
    num = 0
    list=[randint(1,2)for i in range(n)]  # 初始化跳的方式，2为正中心，1为边缘
    list3=[str(i) for i in list] #列表转化为字符串列表
    list2=''.join(list3)
    list1 = re.findall('2+',list2)#找出2或者连续2的几段
    for i in list1:
        num += (-2)*(1-2**len(i))#等比数列前n项和公式
        a+=len(i)
    num=num+n-a
    # num = 0
    # for i in range(n):
    #     if list[i] == 1:  # 边缘直接加一
    #         num += 1
    #     else:
    #         if i == 0:  # 第一次跳在正中心直接加2，防止下一个判断语句越界
    #             a = 2
    #             num += a
    #         elif list[i - 1] == 1:  # 前一次跳边缘，这一次跳正中心，加分不加倍，为2
    #             a = 2
    #             num += a
    #         else:  # 前一次也跳中心，则这次加倍加分
    #             a += 2
    #             num += a
    print(list)
    print("您的最终得分为")
    print(num)
