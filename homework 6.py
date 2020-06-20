import math
g = 9.8
pos_y = lambda v0, theta, t: v0 * math.sin(theta) * t - g * t * t * 1 / 2

first_velocity = float(input('input base velocity: '))
theta = float(input('input launching degree: '))
t = 0

while True:
    t += 0.1
    y = pos_y(first_velocity, theta, t)
    print('t={time}: y={height}'.format(time=t, height=y))
    if y <= 0.0:
        break

print('time', t, 'the CANNON BALL was broke.')