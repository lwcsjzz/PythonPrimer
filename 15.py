import ast
lists = ast.literal_eval(input("请输入列表，用逗号隔开: "))
a = list(reversed(lists))
print(a)