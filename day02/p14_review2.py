# file: review2
# desc: 되새김문제 2, 149~150p

## q01
a= 'Life is too short, you need python'

if 'wife' in a: print('wife')
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif 'need' in a: print('need') # 참이지만 위의 elif문에서 참 값이 리턴되므로 실행X
else: print('none')

## q02
result = 0 
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)

## q03
i = 0
while True:
    i += 1
    if i>5 : break
    print('*' * i)

## q04

for i in range(1, 101):
    print(i)


## q05
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average) 

## q06
numbers = [1,2,3,4,5]
result= [n * 2 for n in numbers if n % 2 == 1] # 실행문, 반복인자, 조건문
print(result)