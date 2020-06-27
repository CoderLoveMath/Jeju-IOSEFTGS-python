s_ev = 0
s_od = 0

for i in range(1, 101):
    if i % 2 == 0:
        s_ev += i
    else:
        s_od += 1

print("even sum", s_ev)
print("odd sum", s_od)