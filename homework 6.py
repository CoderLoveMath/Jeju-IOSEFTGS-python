import math
g = 9.8
pos_y = lambda v0, theta_v, t_v: v0 * math.sin(theta_v) * t_v - g * t_v * t_v * 1 / 2
pos_x = lambda v0, theta_v, t_v: v0 * math.cos(theta_v) * t_v

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