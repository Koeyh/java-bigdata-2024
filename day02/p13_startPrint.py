# file: p13_startPrint.py
# desc: 별찍기
print('예제')
for i in range(1, 6):
    print('*' * i)

# 2중 for문으로 같은 결과 생성
print('\n')

print('별찍기 ------>')

for i in range(1,6) :
    for j in range(6-i, 6) :
        print('*', end='')
    print()

print('역순 쌓기 ------>')
for i in range(1,6) :
    for j in range(i, 6) :
        print('*', end='')
    print()

