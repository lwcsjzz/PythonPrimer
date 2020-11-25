from os import listdir
from os.path import join,isdir,isfile,getctime
from datetime import date, datetime,timedelta
def search(dir,date):
    dirs = [dir]
    while dirs:
        a=dirs.pop(0)
        for sub in listdir(a):
            path = join(a,sub)
            if isfile(path):
                time = str(datetime.fromtimestamp(getctime(path)))
                if time.startswith(date):
                    print(path)
                    print(time)
            if isdir(path):
                dirs.append(path)
search('D:\\',str(date(2017,10,26))[:10])