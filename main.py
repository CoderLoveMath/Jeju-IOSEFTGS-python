num = int(input('Amount of numbers? '))
maxnum = 0

for i in range(num):
    n = int(input('number: '))
    if n > maxnum:
        maxnum = n

print("The greatest number is", maxnum)