# file: p21_example.py
# desc: 연습문제 188p q07
## read() : 문자열로 리턴, 텍스트가 길면 문장이 잘려나온다.
# readline() : 리스트로 리턴
f = open('./day03/test.txt', 'r', encoding='utf-8')
body = f.read() # 문자열이기 때문
f.close()

body = body.replace('java', 'Python')
f = open('./day03/test.txt', 'w')
f.write(body)
f.close()


