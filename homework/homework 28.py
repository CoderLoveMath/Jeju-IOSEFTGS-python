import numpy as np

logo = """
       _____ _               _       _ 
      / ____| |             | |     | |
     | (___ | |__   ___  ___| |_ ___| |
      \___ \| '_ \ / _ \/ _ \ __/ __| |
      ____) | | | |  __/  __/ |_\__ \_|
     |_____/|_| |_|\___|\___|\__|___(_)
                                       
                2020. 7. 11
"""
table = []
y = 0
x = 0

def writedb():
    with open("sheet.sht", "w") as f:
        f.write(str(x) + ' ' + str(y)+ '\n')
        for i in range(int(y)):
            text = ''
            for j in range(int(x)):
                text += table[i][j] + ' '
            f.write(text + '\n')

def file_error():
    print('!-!---------------- WARNING ----------------!-!')
    print('Your file doesn\'t exist or was broken! :(')
    print('Follow this solution to continue.')
    print('Solution: make new file.')
    with open('sheet.sht', 'w+') as f:
        nx = input('width of New file(number): ')
        ny = input('height of New file(number): ')
        init = input('Init value(number): ')
        f.write(nx + ' ' + ny + '\n')
        for i in range(int(ny)):
            text = ''
            for j in range(int(nx)):
                text += init + ' '
            f.write(text + '\n')
    print('Successfully cleared, and now keep going :)')

print(logo)

while True:
    table.clear()

    try:
        with open("sheet.sht", 'r+') as f:
            pro = f.readline().split(' ')
            x = int(pro[0])
            y = int(pro[1])
            for e in f.readlines():
                table.append(' '.join(e[:-1].split(' ')).split())
    except:
        file_error()
        with open("sheet.sht", 'r+') as f:
            pro = f.readline().split(' ')
            x = int(pro[0])
            y = int(pro[1])
            for e in f.readlines():
                table.append(' '.join(e[:-1].split(' ')).split())

    print('----------------------- Menu ---------------------------')
    print('0. New | 1. edit to.. | 2. sort by.. | 3. find | 4. quit')
    print('--------------------------------------------------------')

    """ print like this:
    [3 ] [0] [30] [45] [32]
    [30] [9] [8 ] [7 ] [5 ]
    [0 ] [0] [0 ] [0 ] [1 ]
    """
    try:
        width = np.zeros(x, dtype=int).tolist()
        for j in range(len(table)):
            for k in range(len(table[j])):
                if len(list(table[j][k])) > width[k]:
                    width[k] = len(list(table[j][k]))

        for i in range(len(table)):
            for j in range(len(table[i])):
                print('[' + table[i][j] + ' ' * (width[j] - len(list(table[i][j]))) + ']', end=' ')
            print()
        print('--------------------------------------------------------')
        mod = input('Input mode under Menu (0~4): ')
        if mod == '0':
            print('----------------------- new file -----------------------')
            with open('sheet.sht', 'w+') as f:
                nx = input('width of New file(number): ')
                ny = input('height of New file(number): ')
                init = input('Init value(number): ')
                f.write(nx + ' ' + ny + '\n')
                for i in range(int(ny)):
                    text = ''
                    for j in range(int(nx)):
                        text += init + ' '
                    f.write(text + '\n')
            print('Successfully cleared!')
        elif mod == '1':
            print('--------------------- edit mode ------------------------')
            sy = input('Enter y address to select (1~{}): '.format(y))
            sx = input('Enter x address to select (1~{}): '.format(x))
            value = input('Enter number to change (address is {r}×{c}): '.format(c=sy, r=sx))
            table[int(sy) - 1][int(sx) - 1] = value
            writedb()
            print('Successfully changed!')
        elif mod == '2':
            print('--------------------- sort mode ------------------------')
            print('1. sort x axis (horizontal)')
            print('2. sort y axis (vertical)')
            mod_2 = input('What mode do you want? (1~2): ')
            if mod_2 == '1':
                sort_mod = input('desc? or asc? (D/A): ')
                if sort_mod == 'D':
                    sort_sy = input('Enter y address to select (1~{}): '.format(y))
                    for a in range(x - 1):
                        for b in range(x - a - 1):
                            if int(table[int(sort_sy) - 1][b]) < int(table[int(sort_sy) - 1][b + 1]):
                                table[int(sort_sy) - 1][b], table[int(sort_sy) - 1][b + 1] = table[int(sort_sy) - 1][b + 1], table[int(sort_sy) - 1][b]
                    writedb()
                    print('Successfully sorted!')
                elif sort_mod == 'A':
                    sort_sy = input('Enter y address to select (1~{}): '.format(y))
                    for a in range(x - 1):
                        for b in range(x - a - 1):
                            if int(table[int(sort_sy) - 1][b]) > int(table[int(sort_sy) - 1][b + 1]):
                                table[int(sort_sy) - 1][b], table[int(sort_sy) - 1][b + 1] = table[int(sort_sy) - 1][b + 1], table[int(sort_sy) - 1][b]
                    writedb()
                    print('Successfully sorted!')
                else:
                    print('Wrong Input :( Try again')
            elif mod_2 == '2':
                sort_mod = input('desc? or asc? (D/A): ')
                if sort_mod == 'D':
                    sort_sx = input('Enter x address to select (1~{}): '.format(x))
                    for a in range(y - 1):
                        for b in range(y - a - 1):
                            if int(table[b][int(sort_sx) - 1]) < int(table[b + 1][int(sort_sx) - 1]):
                                table[b + 1][int(sort_sx) - 1], table[b][int(sort_sx) - 1] = table[b][int(sort_sx) - 1], table[b + 1][int(sort_sx) - 1]
                    writedb()
                    print('Successfully sorted!')
                elif sort_mod == 'A':
                    sort_sx = input('Enter x address to select (1~{}): '.format(x))
                    for a in range(y - 1):
                        for b in range(y - a - 1):
                            if int(table[b][int(sort_sx) - 1]) > int(table[b + 1][int(sort_sx) - 1]):
                                table[b + 1][int(sort_sx) - 1], table[b][int(sort_sx) - 1] = table[b][int(sort_sx) - 1], table[b + 1][int(sort_sx) - 1]
                    writedb()
                    print('Successfully sorted!')
                else:
                    print('Wrong Input :( Try again')
            else:
                print('Wrong Input :( Try again')
        elif mod == '3':
            print('--------------------- find mode ------------------------')
            find = input('Enter value to find: ')
            for i in range(y):
                for j in range(x):
                    if table[i][j] == find:
                        print('FIND: location: {x}*{y}'.format(x=i + 1, y=j + 1))
        elif mod == '4':
            break
        else:
            print('Wrong input :(')
    except:
        print('!-!---------------- WARNING ----------------!-!')
        print('Something went wrong :(')
        print('We think this program cannot continue your work,')
        print('and also think this is serious error.')
        print('We have several solution.')
        print('1. delete sheet.sht and restart this program. don\'t worry about message.')
        print('   Just keep going.')
        print('2. restart this program.')
        print('Sorry about this happening :(')
        print('!-!---------------- WARNING ----------------!-!')