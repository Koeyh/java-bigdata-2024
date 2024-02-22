# file: p15_fuction.py
# desc: 함수 학습

def add(a, b): # 리턴값O
    res = a + b
    return res

def sub(a, b): #매개변수는 있으나 리턴값X
    res = a-b
    print(res)

def mul(): #매개변수 X, 리턴값O
    global x, y # 함수 바깥의 전역변수 x, y를 사용
    res = x * y
    return res

def div():
    global x, y
    print(x/y)

def pow(a, b=10): # default 기본 인수는 뒤에 지정해야 함(문법).
    res = a**b # res는 a의 b제곱
    return res

def plus_many(*args): # 동적 매개변수 / 전달받을 매개변수의 개수가 지정되지 않을경우에 사용
    result = 0
    for item in args:
        result += item

    return result

def cal(mode, *args): 
    if mode == 'a': # 더하기
        result = 0
        for i in args:
            result += i

    elif mode == 's': # 뺴기
        result = args[0]
        for i in args[1:]:
            result -= i

    elif mode == 'm': # 곱하기
        result = 1
        for i in args:
            result *=i
    
    elif mode == 'd': # 나누기
        result = args[0]
        for i in args[1:]:
            result /= i

    return result


print('더하기')
x = 10
y = 7
result = add(x, y)
print(result)
sub(x, y)
result = mul()
print(result)
div()

print(pow(3)) # 기본인수
print(plus_many(1,2))
print(plus_many(1,2))
print(plus_many(1,2,3,4,5,6,7,8,9,10))

list1 = range(1,21) # 리스트를 바로 넘겨줄 수 없으니 풀어서 넘겨줌
print(plus_many(*list1))

print(cal('a', 1,2,3,4,5)) # 15 예상
print(cal('s', 100,10,5,5,4)) # 76
print(cal('m', 2,2,2,2,2)) # 32
print(cal('d', 100,5,4,5)) # 1

def print_kwargs(**items): # 키워드 매개변수, 딕셔너리 생성
    print(items)

print_kwargs(name='Peter Parker', age=18, weapon='web shooter')

def cal2(a, b):
    res1 = a+b
    res2 = a-b
    res3 = a*b
    res4 = a/b
    return res1, res2, res3, res4

(a, b, c, d) = cal2(3, 4) # 튜플에 여러개의 리턴값을 한번에 받아낼 수 있다.
print(a, b, c, d)


## 익명함수 람다함수
add = lambda a, b: a+b
print(add(5,4))
