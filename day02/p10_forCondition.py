# file: p10_forCondition.py
# desc : for 반복문

# for item in 반복할객체 :
# 실행문

a = [1,3,5,7,9]
print(type(a))

for i in a:
    print(type(i))

b = [(1,2), (3,4), (5,6)] # tuple의 리스트
for i in b :
    print(i)

for first, second in b : # (first, second) 튜플의 괄호는 생략 가능
    print(first, second)


# 평균 내기
grade = [90, 80, 50, 70, 10]
sum = 0
for i in grade:
    sum += i

print("점수 총합 :", sum)
print("평균 :",sum / len(grade))

## range()
print(range(10))
print(range(0, 10))

for i in range(0, 10) :
    print(i, end=', ')
print()

print(list(range(0,10)))

print(list(range(0,11, 2))) # 0부터 10까지 2씩
print(list(range(1,10,2)))

print(list(range(10,0,-2)))
print(list(range(4, 101, 4)))

res = 0
for i in range(1, 1001):
    res += i

print(res)

## list comprehesion \ 리스트 내포
# list(range()) 만으로도 리스트를 생성할 수 있지만 여러조건으로 리스트를 생성할 떄에는 리스트 컴프리헨션을 적용하는것이 좋음
print([i for i in range(1, 1001)])
print(list(range(1,1000))) # 위와 동일

print([num * 3 for num in range(1, 1001) if num % 3 == 0])

score = 60

# 파이썬에서는 조건 연산자를 잘 쓰지 않는다
print('success' if score >=60 else 'failure')