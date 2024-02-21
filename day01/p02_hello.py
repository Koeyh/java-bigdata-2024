# file: p02_number.py
# desc: 숫자형 자료타입

#일반 숫자형
age = 40 # int형 담는 변수
taxRate = 8.8 #float형 담는 변수

highFloats = 4.24E10 # 지수승(float)

# Python은 char형이 없이 무조건 문자열
print("나이는 : ", age) # 문자열 "" ,'' 사용 가능
print("세율 : " ,taxRate) 
print("지수값 : ",highFloats)

# 틀수 숫자형
binVal = 0b11111111 #255
octVal = 0o11 # 9, 8진수 표기
hexVal = 0xFF # 65, 16진수 표기
print('2진수', binVal, '8진수', octVal, '16진수', hexVal)

# 사칙연산은 자바와 큰 차이 없음
a, b, c = 3, 4, 5
print(a+b)
print(a-b)

print(a*c) # 일반 곱셈
print(2 ** 10) # 2의 10제곱 import math; math.pow()

# 단, 나눗셈은 3가지로 분류
print(c/b) # 정확하게 실수로 나누기
print(c//b) # 정수로만 나누기
print(c % b) # 나머지

print((a+b) * c) # 연산자 우선순위는 괄호로 정리할 것