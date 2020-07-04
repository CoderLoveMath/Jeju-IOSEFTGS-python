strlist = []
n = int(input('Total Count: '))
for i in range(n):
    strlist.append(input('String: '))

for i in range(n):
    if len(strlist[i]) <= 3 or strlist[i].find('zzz') != -1:
        print(strlist[i], ': X')
    else:
        print(strlist[i], ': O')