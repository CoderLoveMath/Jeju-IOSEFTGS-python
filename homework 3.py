m = int(input('input minute time: '))   # input
d = m // 720    # day
m = m % 720
h = m // 60 # hour
m = m % 60  # minute

print(d, 'day', h, 'hour', m, 'minute')    # output (d)hour (h)hour (m)minute
