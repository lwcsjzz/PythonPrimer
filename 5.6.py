def count(a , b =1):
    c = a
    while True :
        yield c
        c+=b
for i in count(3,2):
    print(i)