s = int(input('input second time: '))   # input
h = s // 360    # hoour
s = s % 360
m = s // 60 # minute
s = s % 60  # second

print(h, 'hour', m, 'min', s, 'sec')    # output (h)hour (m)minute (s)second
