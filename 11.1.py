try:
    with open(r'result.txt', "w", encoding="UTF-8") as re:
        try:
            with open(r"file1.txt","r+",encoding="UTF-8") as  f1, open(r'file2.txt',"r+",encoding="UTF-8")as f2:
                while True:
                    lines1 = f1.readline()
                    lines2 = f2.readline()
                    if lines1 or lines2:
                        if lines1:
                            re.write(lines1)
                        if lines2:
                            re.write(lines2)
                    else:
                        break
        except:
            print("无法打开")
except:
    print("无法建造")