import ast
num_dict = {}
num = ast.literal_eval(input("请输入列表，用逗号隔开: "))
for i in num:
    if i not in num_dict:
        num_dict[i]=1
for i in num_dict:
    print(i)