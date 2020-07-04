text = ' 제주대,서울대,KAIST '
text = text.strip()
text = text.replace('대', '대학교')
text = text.split(',')

print(text)