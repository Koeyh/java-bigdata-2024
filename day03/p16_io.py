# file: p16_io.py
# desc: 입/출력

# input() 함수 기본
# res = input("인사말을 적으세요 > ")

#print(res)

# input() 함수로 받는 값은 모두 문자열(str)
#num = input('곱할 수를 적으세요 > ')
#print(type(num))
#num = int(num) 
# 숫자를 입력받아 계산등을 할 때는 형 변환(str ->int) 필요
#print(num*2)

#num = int(input('2로 곱할 숫자 입력 > ')) # 정수형 입력 외에는 모두 오류 발생
#print(num * 2)

## 여러개의 값 입력 (튜플 사용)

# 튜플의 괄호중 할당을 받는 쪽의 괄호는 생략 가능
#(a1, a2, a3) = input('합산 할 세 값을 입력(구분자 space) > ').split(' ')
a1, a2, a3 = map(int, input('합산 할 세 값을 입력(구분자 space) > ').split(' '))

print(a1)
print(a2)
print(a3)
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
sum = a1+a2+a3
print(f'합계는 {sum}')
