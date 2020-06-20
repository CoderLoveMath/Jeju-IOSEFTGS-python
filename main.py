cm = int(input('input cm: ')) # stdin: cm
print('converting...')
m = cm // 100   # m = 100cm
cm = cm % 100   # cm = (input) mod 100
print('convert finished. The result is ', m, 'm ', cm, 'cm', sep='') # stdout: (m)m (cm)cm