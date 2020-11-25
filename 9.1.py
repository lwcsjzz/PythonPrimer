with open(r'result.txt', "w", encoding="UTF-8") as result:
    with open(r'file1.txt', "r+", encoding="UTF-8") as f1, open(r'file2.txt', "r+", encoding="UTF-8") as f2:
        while True:
            lines1 = f1.readline()
            lines2 = f2.readline()
            if lines1 or lines2:
                if lines1:
                    result.write(lines1)
                if lines2:
                    result.write(lines2)
            else:
                break
