nat = ['Korea', 'United States', 'England', 'Japan', 'China']
cap = ['Seoul', 'Washington D.C', 'London', 'Dokyo', 'Beijing']

while True:
    ans = input('Nation name or Exit: ')
    if ans == "Exit":
        break
    elif ans in nat:
        print(cap[nat.index(ans)])
    else:
        print('Anomymous Nation name')