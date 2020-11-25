file = '9.1.py'
with open(file, 'r', encoding='UTF-8') as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))
lines = [line.rstrip().ljust(maxLength + 5) + '#' + str(index) + '\n'
         for index, line in enumerate(lines)]
with open(file[:-3] + '_new.py', 'w', encoding='UTF-8') as fp:
    fp.writelines(lines)