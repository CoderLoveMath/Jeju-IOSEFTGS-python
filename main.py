problem = ['Who is the king of animals? ', 'Who is the king of birds? ', 'who is the king in sea? ']
answer = ['Lion', 'Eagle', 'Whale']

for i in range(len(problem)):
    ans = input(problem[i])
    if ans == answer[i]:
        print("Ding Dong Dang!")
    else:
        print("Brrrrrrrrrrrrr")