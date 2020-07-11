food = [['사과', 700], ['감귤', 300], ['바나나', 500]]

for a in range(len(food)-2,-1,-1):
  for b in range(a+1):
    if food[b + 1][0] < food[b][0]:
      food[b], food[b+1] = food[b+1], food[b]
print('가나다순:', end=' ')
for i in range(len(food)):
  print(food[i][0], food[i][1], end='  ')
print()

for a in range(len(food)-2,-1,-1):
  for b in range(a+1):
    if food[b][1] < food[b + 1][1]:
      food[b], food[b+1] = food[b+1], food[b]
print('가격역순:', end=' ')
for i in range(len(food)):
  print(food[i][0], food[i][1], end='  ')