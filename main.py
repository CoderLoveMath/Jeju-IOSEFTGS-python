problem = ['Who is the king of animals? ', 'Who is the king of birds? ', 'Who is the king in sea? ',
           'What programming language are we using? ', 'Is watermelon fruit? ', '(3 * 5) / 2 + 6 / 2 = ? ',
           'Monday, Tuesday, ? ', 'Who is the president of South Korea? ', 'What year was Korean war started?', 'What programming language was made in Jetbrain IDE?']
answer = ['lion', 'eagle', 'whale', 'python', 'no', '7', 'wednesday', 'moon jae in', '1950', 'java']

for i in range(len(problem)):
    ans = input(problem[i])
    if ans == answer[i]:
        print("Ding Dong Dang!")
    else:
        print("Brrrrrrrrrrrrr")