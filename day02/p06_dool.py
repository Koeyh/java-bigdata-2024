# file: p06_dool.py
# desc: 불 타입 학습

# 참, 거짓

a = True # true
b = False

print(a)
print(type(a)) # <class 'bool'>
print(type(1)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type('Hi')) # <class 'str'>
print(type([1, 2, 3])) # <class 'list'>
print(type((1, 2, 3))) # <class 'tuple'>

print(a == b)
print(a == (not b))

print(bool('H'))
# 참/거짓 구분 빈값, 0, None False 그외 True

# None 타입
None

c = None
a = 1
b = 0
print(c)
print(a + b) # True(1) False(0)
c = 3 # 기존에 None타입으로 지정한 변수에 값을 대입할 수 있음
print(c + a) # 실제적인 값이 주어지지 않은 None타입은 연산이 불가능함

