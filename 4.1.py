n = int(input("请输入一个n"))
num=[]
i=2
for i in range(2,n):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break1
   else:
      num.append(i)
print(num)