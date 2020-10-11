import random
lists = []
while(len(lists) != 20):
    lists.append(random.randint(1,50))
for i in range(20):
    for j in range(i):
        if lists[i]<lists[j]:
            for k in range(j,i):
                lists[k],lists[i]=lists[i],lists[k]
print(lists)
