def reversedq(list):
    for i in list[::-1]:
        yield i

a = input()
print(list(reversedq(a)))