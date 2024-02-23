# file: p25_exmaple.py
# desc: 연습문제 185p, q01 ~ q06

# # q01
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
    
# # q02
def avg_numbers(pass):
    result = 0
    for i in args:
        result += i
    return pass

avg_numbers(1, 2)
avg_numbers(1,2,3,4,5)

 # q03 사용자 입력 시 형 변환 문법
input1 = input('첫 번째 숫자를 입력하시오: ')
input2 = input('두 번째 숫자를 입력하시오: ')

input1 = int(input1)
input2 = int(input2)

total = input1 + input2
print(f'두 수의 합은 {total} 입니다.')

# q04 출력형태 판단
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you" + "need" + "python"])) # 공백 포함

# q05
f1 = open('./day03/test.txt', 'w')
f1.write('Life is too short')
f1.close()

f2 = open('./day03/test.txt', 'r')
read = f2.read()
f2.close()
print(read)

# q06
user_input = input('저장할 내용을 입력하세요:')
f = open('./day03/test.txt', 'w')
f.write(user_input)
f.write('\n')
f.close()

f = open('./day03/test.txt', 'r')
read = f.read()
f.close()
print(read)
