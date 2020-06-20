s = int(input('input second time: '))   # input
h = s // 360
s = s % 360
m = s // 60
s = s % 60

print(h, 'hour', m, 'min', s, 'sec')
