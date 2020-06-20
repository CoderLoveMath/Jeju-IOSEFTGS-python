from math import *
from matplotlib import pyplot as plt
import time

print("""
   _____                                 _____ _                 _       _   _             
  / ____|                               / ____(_)               | |     | | (_)            
 | |     __ _ _ __  _ __   ___  _ __   | (___  _ _ __ ___  _   _| | __ _| |_ _  ___  _ __  
 | |    / _` | '_ \| '_ \ / _ \| '_ \   \___ \| | '_ ` _ \| | | | |/ _` | __| |/ _ \| '_ \ 
 | |___| (_| | | | | | | | (_) | | | |  ____) | | | | | | | |_| | | (_| | |_| | (_) | | | |
  \_____\__,_|_| |_|_| |_|\___/|_| |_| |_____/|_|_| |_| |_|\__,_|_|\__,_|\__|_|\___/|_| |_|
                                start in 3 seconds
""")
time.sleep(3)

# hyper parameter
g = 9.8

# parameter
v0 = float(input('launching velocity(ms/s): '))
deg = float(input('launching degree(˚): ')) / 45
x_range = int(input('checking distance: '))

# var
x = range(0, x_range)
y = []

# calc func
def calcY(x_):
    first_term = x_ * tan(deg)
    operation = lambda t1, t2: t1 - t2
    second_term = g * x_ * x_ / ( 2 * v0 * v0 * cos(deg) * cos(deg))
    return operation(first_term, second_term)

for i in x:
    y.append(calcY(i))

plt.plot(x, y)
plt.show()