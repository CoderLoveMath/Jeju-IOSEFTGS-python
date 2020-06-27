# Cannon Simulation ver 1
# 반갑습니다. 이 시뮬레이션은 물체의 질량, 공기저항을 제외하였을때 (한마디로 우주라고 가정합니다)에서 어떤궤도로 포탄이 날아가는지
# matplotlib을 이용해 보여주는 프로그램입니다. 코드의 양이 많음에 따라 github 링크로 보내는 점 널리 양해해주시기 바랍니다.
# How to use
# 1. parameter을 작성합니다. 첫번째는 속도, 두번째는 각도 (최대 90도이며 오른쪽 기준), 세번째는 유저가 확인할 범위를 말합니다.
# 2. 팝업창을 확인합니다.
# 3. 끝! 간단하죠?


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
    second_term = g * x_ * x_ / (2 * v0 * v0 * cos(deg) * cos(deg))
    return operation(first_term, second_term)

for i in x:
    y.append(calcY(i))

plt.plot(x, y)
plt.show()