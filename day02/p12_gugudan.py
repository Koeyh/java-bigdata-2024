# file: p12_gugudan.py
# desc: 구구단 프로그램

print('구구단 프로그램 v99')
for x in range(2, 10) : # 단, 2~9
    print(f'{x}단 시작 ----->')
    for y in range(1, 10) : # 1~9
        print(f'{x} * {y} = {x*y:2d} |', end = '\t')
    print() # 단순 개행

