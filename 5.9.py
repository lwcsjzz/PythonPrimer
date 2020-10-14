def any(a):
    for b in a:
        if b:
            return True
    return False
a = input()
print(all(a))