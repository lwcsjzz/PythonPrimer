import os
import filecmp
import shutil
import sys
def usage():
    print('scrdir和dstdir必须存在')
    sys.exit(0)

def autoBackup(scrDir, dstDir):
    try:
        for item in os.listdir(sceDir):
            scrItem = os.path.join(scrDir, item)
            dstItem = scrItem.replace(scrDir,dstDir)
            if os.path.isdir(scrItem):
                if not os.path.exists(dstItem):
                    os.makedirs(dstItem)
                    print('make ditectory'+dstItem)
                autoBackup(scrItem,dstItem)
            elif os.path.isfile(scrItem):
                if ((not os.path.exists(dstItem))\
                        or(not filecmp.cmp(scrItem, dstItem, shallow=False))):
                    shutil.copyfile(scrDir,dstItem)
                    print('file:'+scrItem+'==>'+dstItem)
    except:
        usage()
if __name__=='__main__':
    if len(sys.argv)!=3:
        usage()
    scrDir, dstDir=sys.argv[1],sys.argv[2]
    autoBackup(scrDir,dstDir)