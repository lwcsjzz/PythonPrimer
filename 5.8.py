def all(a):
    for b in a:
        if not b:
            return False
    return True
a = input()
print(all(a))