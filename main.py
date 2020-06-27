import random
num = random.randint(1, 20)

while True:
    select = int(input('Guess my number!'))

    if select is num:
        print("Right. You're genius!")
        break
    elif num < select:
        print('it is less then your number,', select)
    else:
        print('it is greatest then your number,', select)
