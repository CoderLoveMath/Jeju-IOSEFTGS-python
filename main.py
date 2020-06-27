menu = ['짜장면', '짬뽕', '볶음밥', '우동']

for i in range(len(menu)//2):
    menu[i], menu[3 - i] = menu[3 - i], menu[i]

print(menu)