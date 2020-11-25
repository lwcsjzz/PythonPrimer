from os import listdir
from os.path import join,isdir
def search(dir,file):
    dirs = [dir]
    while dirs:
        a=dirs.pop(0)
        for sub in listdir(a):
            if sub == file:
                return True
            path = join(a,sub)
            if isdir(path):
                dirs.append(path)
    return False
print(search('D:\\','temp.txt'))