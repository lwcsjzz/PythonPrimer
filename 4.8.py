import ast
num = ast.literal_eval(input("请输入列表，用逗号隔开: "))
n = num[1]-num[0]
for i in range(len(num)):
    for j in range(i+1):
        if (num[i]-num[j])>n:
            n = (num[i]-num[j])
print(n)
