Logo = """
  ______                              _                               _ 
 / _____)                            | |                             | |
( (____    ____   ___    ____  _____ | |__    ___   _____   ____   __| |
 \____ \  / ___) / _ \  / ___)| ___ ||  _ \  / _ \ (____ | / ___) / _  |
 _____) )( (___ | |_| || |    | ____|| |_) )| |_| |/ ___ || |    ( (_| |
(______/  \____) \___/ |_|    |_____)|____/  \___/ \_____||_|     \____|
                            VER 1.0.0 - CUI
"""

userlist = []
print(Logo)

try:
    f = open('db.dat', 'r')
    li = f.readlines()
    for i in range(len(li)):
        li[i] = li[i].strip('\n')
        userlist.append(li[i].split('^&*'))
        userlist[i][1] = int(userlist[i][1])
    f.close()
except:
    pass

print('----------------- All data saved ------------------')

with open('db.dat', "w") as f:
    while True:
        n = int(input("""
        1. add student's data
        2. delete student's data
        3. edit student's data
        4. clear all
        5. print as Grade Order
        6. print as Name Order
        7. save and quit
        """))

        if n == 1:
            userinfo = [input("Enter student's name: "), input("Enter student's grade: ")]
            userlist.append([userinfo[0], int(userinfo[1])])
            print('thanks! your data was saved!')
        elif n == 2:
            userinfo = input("Enter student's name to delete: ")
            for i in range(len(userlist)):
                if userlist[i][0] == userinfo:
                    del userlist[i]
            print('thanks! successfully deleted!')
        elif n == 3:
            userinfo = input("Enter student's name to edit: ")
            for i in range(len(userlist)):
                if userlist[i][0] == userinfo:
                    changescore = int(input("Enter student's grade again: "))
                    userlist[i][1] = changescore
            print('thanks! successfully edited!')
        elif n == 4:
            arusure = input('Are you sure to clear? (Y/N): ')
            if arusure == "Y":
                userlist = []
                print('thanks! successfully cleared!')
            else:
                print('your data was not cleared.')
        elif n == 5:
            for a in range(len(userlist) - 2, -1, -1):
                for b in range(a + 1):
                    if userlist[b][1] < userlist[b + 1][1]:
                        userlist[b], userlist[b + 1] = userlist[b + 1], userlist[b]
            for i in range(len(userlist)):
                print('name: {name}, grade: {score}'.format(name=userlist[i][0], score=userlist[i][1]))
        elif n == 6:
            for a in range(len(userlist) - 2, -1, -1):
                for b in range(a + 1):
                    if userlist[b][0] > userlist[b + 1][0]:
                        userlist[b], userlist[b + 1] = userlist[b + 1], userlist[b]
            for i in range(len(userlist)):
                print('name: {name}, grade: {score}'.format(name=userlist[i][0], score=userlist[i][1]))
        elif n == 7:
            print('saving...')
            for i in range(len(userlist)):
                f.write(str(userlist[i][0]) + '^&*' + str(userlist[i][1]))
            print('saving finished :)')
            break
        else:
            print('Enter again... :(')



